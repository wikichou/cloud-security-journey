今天要的目標是要完成一個資安的重要核心思維:**縮小攻擊面**。
攻擊面再說的一個系統暴露給攻擊者可以被利用的入口跟資源的總和，簡單來說假設系統是一棟房子，那攻擊面就可能有:
- 門窗(對外的 port、服務)
- 工具(shell、package manager、各種指令)
- 住在裡面的人有多大權限(root 還是一般使用者)
今天要做的兩個縮小攻擊面的練習有
1.降低住戶權限(非root)
2.清空工具(minimal image)

### 非root
docker container預設適用root在執行應用程式，這會造成一個大問題，***應用被打穿時，攻擊者就是root***，這也意味著攻擊者直接可以讀寫安裝任何東西，更進一步來說，要是今天container的設定不當，有可能會發生container escape的狀況(例如掛載了 host 目錄、給了危險的 capability)，變成整台機器都被攻擊者控制。

昨天的docker file長這樣
```
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

這樣的配置跑起來就會直接使用root執行app，所以我們得要加入一個新的使用者並直接切換過去

```
RUN useradd --create-home --shell /bin/bash nonroot 
USER nonroot
```
- `RUN useradd --create-home --shell /bin/bash nonroot` — 在 build image 的時候,建立一個叫 `nonroot` 的一般使用者(這一步還是用 root 跑的,因為建帳號本身需要權限)。`--create-home` 幫它建家目錄。
- `USER nonroot` — 這行是關鍵。**從這行之後的所有指令,包括最後 `CMD` 執行你的 app,都會用 `nonroot` 這個身份跑**。這就是「切換住戶」的動作。

因為上面兩點，所以要注意順序，如果有其他要權限的操作也要放在他們之前![[nonroot2.png]]
![[nonroot.png]]
如果前面的docker file有被正確配置，那跑起來就應該是nonroot，並且UID也不是0，這就代表即便今天service被打穿了，也只會影響到這個service本身而不會破壞整個container。


### minimal base image
我們的docker file第一行就寫著
```
FROM python:3.12-slim
```

這決定了container裡面內建了哪些東西，用不同的base image的差異非常大，以python舉例:

- **完整版(`python:3.12`)** — 裡面有完整的 shell(bash)、package manager(apt)、各種系統工具(curl、wget…)。方便,但這些工具**攻擊者也能用**。
- **slim 版(`python:3.12-slim`,你現在用的)** — 砍掉大部分非必要工具,但還留著基本 shell。
- **distroless(`gcr.io/distroless/python3`)** — 只留下跑你程式的最低限度,**連 shell、package manager 都沒有**。

distroless沒有shell這件事情在資安上是一個很大的優勢，因為攻擊者如果拿到RCE(遠端執行程式碼)的能力之後通常會

	1.開一個互動式 shell 站穩腳步
	2.用 package manager 或 curl/wget 下載更多攻擊工具
	3.從這台橫向移動到其他系統

而沒有shell的話，第一第二步就直接做不了了，就算攻擊者真的注入了程式碼，環境裡也沒有sh/bash/apt/curl這些東西，導致操作變得很困難，以此就達到的縮小攻擊面的目的

![[python distroless.png]]