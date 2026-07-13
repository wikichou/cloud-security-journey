之前練習時都只起了一個container，但這周的目標是要nginx + Flask + Redis 三個同時啟動串起來，要是按照之前的做法得要自己下三次docker run，還要自己管理連線狀況等等，而compose則是可以只用一個yaml檔把所有配置都先寫好，一次一起跑起來，也就是管理多容器的工具

### example: docker-compose.yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
  echo:
    image: hashicorp/http-echo
    command: ["-text=hello from echo"]
    ports:
      - "5678:5678"
就會等於
docker run -d --name web -p 8080:80 nginx:alpine
docker run -d --name echo -p 5678:5678 hashicorp/http-echo -text="hello from echo"

這麼做的好處很直接
- **可以存進 GitHub**,跟你的 code 一起版控(這也是你路線圖裡一直強調「作品集」的原因之一——別人看你的 repo 就知道你怎麼設計架構)
- **一個指令啟動全部**:`docker compose up -d`,不用背順序、不用手動打三次
- **改設定不用重敲指令**,直接改 yaml 檔案裡的值

會分為四大區塊
- `services`：定義每個容器（image、build、ports、環境變數）
- `networks`：容器間的網路，Compose 預設會幫你建一個
- `volumes`：資料持久化或掛載
- `depends_on`：控制啟動順序（注意：只保證「啟動順序」，不保證裡面的服務「已經 ready」）

利用
```
docker compose up
```
啟動前面的yaml之後就可以去看看我們啟動起來的東西，例如說docker compose ps看到
![[ps.png]]
或是logs看到
![[logs.png]]
又或著是可以去看看實際server有沒有被跑起來
![[echo.png|262]]![[nginx.png|364]]
