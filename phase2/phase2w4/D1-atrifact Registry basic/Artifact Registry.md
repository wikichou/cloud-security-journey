在知道神麼是artifact registry之前，要先明白甚麼是docker的registry

#### Registry
前面我們練習了自己build一個image，而這個image是被儲存在本機的docker daemon裡面，一但想要換電腦，或是部屬到cloud上面，就必須要尋求別的手段。

image不像是code 一樣可以直接push到git上面，因為它是一包二進制的檔案，git並不適合存，所以Registry出現了，專門用於存放/分發container image的伺服器。
```
code    →  git push  →  GitHub        →  git clone
image   →  docker push → Registry     →  docker pull
```
事實上，之前練習docker compose up的時候，看到的很多pulling就是從docker hub拉下來的東西，docker hub就是docker官方營運的公開registry，也是docker CLI的預設值，只要 image 名稱前面沒有寫 registry 網域，Docker 就預設去 `docker.io` 找。


#### container registry
Google 早期的 container registry 服務，網域是 `gcr.io`。用起來像這樣：
```
gcr.io/my-project/myflask:v1
```
**它的實作方式是關鍵**：Container Registry 不是一個真正獨立的服務，它底層其實就是一個 **Cloud Storage bucket**。你第一次 push image 到 `gcr.io`，GCP 會偷偷在你的 project 裡建一個叫 `artifacts.my-project.appspot.com` 的 GCS bucket，image 的每一層 layer 就是那個 bucket 裡的檔案。

#### 這個實作帶來的三個問題

**問題 1：權限只能到 project 層級（最嚴重）**

因為所有 image 都在**同一個 bucket** 裡，而 IAM 權限是綁在 bucket 上的。所以你給某個 service account「能推 image」的權限，實際上是給了它整個 bucket 的寫入權——

> 意思是：你的 CI/CD service account 一旦能推 dev 的 image，它**同時也能推 production 的 image**。做不到區分。

這在資安上是很糟的狀況。想像 CI pipeline 被入侵（Phase 3 你會學到供應鏈攻擊，Phase 5 W5-6 整個主題就是這個），攻擊者拿到那把鑰匙，就能直接覆蓋你的 production image。

**問題 2：只能存 container image**

現代專案不只有 image，還有 Maven jar、npm 套件、Python wheel。這些要另外找地方放。

**問題 3：region 選擇很少**

只有 `gcr.io`(us)、`us.gcr.io`、`eu.gcr.io`、`asia.gcr.io` 四個 multi-region。資料落地位置控制不精細，這在有合規要求時（Phase 6 會學 GDPR、資料落地）是問題。

因為這些問題，所以第二代的artifact registry就出現了

#### Artifact Registry（`pkg.dev`）

Google 重寫的版本，把上面三個問題全部解掉。這是現在的標準，Container Registry 已經進入淘汰狀態，新專案一律用 Artifact Registry。

Artifact Registry 引入了一個 Container Registry 沒有的東西：**Repository**。層級長這樣：
```
Project（my-project）
 ├── Repository: dev-images      ← 權限可以獨立設在這一層
 │    ├── myflask
 │    └── myapi
 └── Repository: prod-images     ← 這裡設不同的權限
      └── myflask
```
依照這個分級，就可以
dev-images   → CI service account 有 writer（可推）
prod-images  → CI service account 只有 reader（只能拉，不能推）
             → 只有 release pipeline 的 SA 有 writer

這就是「最小權限原則」在 registry 上的具體實作。

| | Container Registry | Artifact Registry |
|---|---|---|
| 網域 | `gcr.io` | `LOCATION-docker.pkg.dev` |
| 底層 | GCS bucket（借來的） | 原生 GCP 資源型別 |
| 權限粒度 | project 層級（整個 bucket） | per-repository |
| 存什麼 | 只有 container image | image + Maven / npm / Python / apt / yum |
| Location | 4 個 multi-region | 任意 region + multi-region |

一個artifact registry名字大概長這樣
```
us-central1-docker.pkg.dev / my-project / dev-images / myflask : v1
└──────────┬───────────┘   └────┬────┘  └────┬────┘  └──┬──┘  └┬┘
      registry 網域          PROJECT ID    REPO 名稱   IMAGE  TAG
      （含 location）
```

注意到最後一欄的tag，docker tag只是給同一份 image 掛第二個名字。就像 git 的 branch 指標指向同一個 commit。
既然 tag 只是個指標，別人（或攻擊者）就可以把 `myflask:v1` 這個 tag **重新指到另一個 image**。你的部署設定寫著 `myflask:v1`，內容卻已經被換掉了。
因此，可以改用digiest，Digest 是內容的 SHA-256 雜湊值，無法被偽造。
```
us-central1-docker.pkg.dev/my-project/dev-images/myflask@sha256:a1b2c3...
                                                        ↑ 注意是 @ 不是 :
```
內容變了，digest 必定變。所以 digest 是 **immutable reference**（不可變引用）——你指定某個 digest，拿到的一定是那份內容。