首先，要先說明一下wsl
**WSL2(Windows Subsystem for Linux 2)= 微軟在 Windows 裡,用輕量 VM 跑一個真正的 Linux kernel,讓你能在 Windows 上直接執行 Linux 程式。**

關鍵字是**「真正的 Linux kernel」**——這是它跟前一代 WSL1 最大的差別,也是為什麼 Docker 一定要它。

docker本身則是一套工具鏈,幫你(1)打包應用成標準化的 image、(2)分發 image、(3)用 namespace + cgroup + capability 把 image 跑成隔離的 container。
## 容器 vs VM

| | VM（VirtualBox） | Container（Docker） |
|---|---|---|
| Kernel | 每個 VM **自己一套完整 kernel** | **共用 host kernel** |
| 隔離手段 | Hypervisor 虛擬化硬體 | namespace + cgroup + capability |
| 啟動速度 | 慢（要開機整個 OS） | 快（秒級，只是跑個 process） |
| 資源開銷 | 重（整套 OS） | 輕 |
| 隔離強度 | **強**（逃逸很難） | **相對弱**（逃逸 = 突破 kernel 隔離） |

> **關鍵**：容器共用 host kernel，所以「容器逃逸（escape）」的本質是**突破那層 kernel 隔離**——這也是為什麼容器安全設定（cap-drop、非 root、read-only）如此重要。

## Image vs Container
整個 Docker 世界的基礎。

> **Image = class(唯讀模板);Container = instance(執行實例)。**  
> 一個 image 可以 `docker run` 出很多個 container,就像一個 class 可以 `new` 出很多 object。


### Image:唯讀的、一層層疊起來的模板

#### 本質

Image 是一個**靜態、唯讀、可重複使用的打包產物**。裡面裝著:

- 應用程式的 code
- 所有依賴(套件、library)
- 執行環境(base OS 的檔案系統,如 `python:3.12-slim`)
- metadata(預設要執行什麼指令、開哪個 port)
#### 關鍵特性一:image 是「分層(layer)」的

這是 image 最重要的結構特性。Dockerfile 每一個指令,build 時都疊出一個**唯讀 layer**:

dockerfile

```dockerfile
FROM python:3.12-slim                  # ← 基礎層(可能本身就是好幾層)
WORKDIR /app                           # ← layer
COPY requirements.txt .                # ← layer
RUN pip install -r requirements.txt    # ← layer(最重的一層)
COPY . .                               # ← layer
CMD ["python", "app.py"]               # ← metadata,不是資料層
```

**每一層都是唯讀的,且只記錄「相對於前一層的變化」**(類似 git commit 的 diff 概念)。

#### 關鍵特性二:layer 可以被共用與快取

因為每層唯讀且有唯一識別,所以:

- **跨 image 共用**:十個 image 都 `FROM python:3.12-slim`,那層在磁碟上**只存一份**,大幅省空間
- **build 快取**:重 build 時,只要某層的輸入沒變,Docker 直接重用快取(顯示 `CACHED`)

### Container:image 疊上「可寫層」後跑起來的實例

#### 本質

Container = **image(唯讀層們)+ 一層可寫層(writable layer)+ 一組 namespace/cgroup/capability**,然後跑起一個 process。

```
┌─────────────────────────┐
│  可寫層 (Writable)      │  ← 只有 container 有,你在容器裡的所有改動寫這裡
├─────────────────────────┤
│  layer 4  (唯讀)        │  ┐
│  layer 3  (唯讀)        │  │
│  layer 2  (唯讀)        │  ├── 來自 image,唯讀、可被多個 container 共用
│  layer 1  (唯讀)        │  ┘
└─────────────────────────┘
   + namespace + cgroup + capabilities  ← 這週學的三根支柱,由 docker run 組裝
```

#### 關鍵特性一:可寫層是 container 獨有的

你在容器裡 `touch` 一個檔案、改一份設定、寫一筆 log——**全部寫進那層可寫層**,不會動到底下的 image。這就是為什麼:

- **同一個 image 開出的多個 container 互不干擾**:各有各的可寫層
- **`docker rm` 刪掉容器,可寫層就消失**,改動全沒了(除非用 volume 持久化)
- **image 永遠保持乾淨**:不管容器裡怎麼搞,image 本身不變

> 這種「唯讀層 + 上面疊一層可寫」的機制叫 **copy-on-write(CoW)**:你要改某個檔案時,才把它從唯讀層複製到可寫層再改。沒改的檔案就直接讀底下的唯讀層,不佔額外空間。

`docker run` 做的事就是:把 image 的唯讀層攤開 → 疊一層可寫層 → 建六個 namespace + 一個 cgroup node + 設好 capability → 在裡面啟動 process。

```
docker ps -a       # 所有容器(含已停止的)
docker images      # 本機有哪些映像
```

![[docker ps -a.png]]

![[docker images.png]]
