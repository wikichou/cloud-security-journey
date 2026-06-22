### Cloud Storage

雲端上的應用程式存檔案的地方
- 網站的圖片
- 使用者上傳的檔案
- 資料庫的備份
- Log 檔案歸檔
這些都需要一個「雲端的儲存空間」，這就是 Cloud Storage。

**Bucket** = 最上層的容器，類似一個雲端硬碟空間

- 名稱**全球唯一**（全世界所有 GCP 用戶共用一個命名空間，所以你前天取 `practice-0610` 這種名字有可能跟別人撞名）
- 屬於某個 Project（還記得資源層級嗎：Project → Resource，bucket 就是一種 Resource）

**Object** = 放在 bucket 裡的檔案

- 一張圖、一個 zip、一個 log 檔，任何檔案都是 object
- 沒有真正的「資料夾」概念，`photos/2026/cat.jpg` 整串其實是檔名，只是介面上顯示成資料夾的樣子
### Access Control
bucket 建好了，檔案放進去了，接下來的問題是：

> **誰**可以對這些檔案做**什麼事**？

- 誰可以讀（下載）？
- 誰可以寫（上傳、覆蓋）？
- 誰可以刪？
- 誰可以改權限設定本身？

控制這些的機制就叫「存取控制」（Access Control）。這不是 Cloud Storage 獨有的概念，整個資安領域都圍繞這件事轉，你之後學的 IAM、RBAC、防火牆規則，本質上都是存取控制。

#### 存取控制的三個基本元素

任何存取控制都由三個東西組成：

```
誰（Principal） + 能做什麼（Permission） + 對什麼東西（Resource）
```

| Principal 類型                | 例子                                    | 說明                |
| --------------------------- | ------------------------------------- | ----------------- |
| Google 帳號                   | `chris@gmail.com`                     | 一個具體的人            |
| Service Account             | `app@project.iam.gserviceaccount.com` | 程式的身份（Phase 4 重點） |
| Google 群組                   | `team@company.com`                    | 一群人               |
| **`allAuthenticatedUsers`** | —                                     | ⚠️ 特殊             |
| **`allUsers`**              | —                                     | ⚠️ 特殊             |
**`allUsers` = 全世界任何人**

- 不需要登入任何帳號
- 路人打開瀏覽器輸入網址就能存取
- 把它加進權限 = 把檔案放上公開網路

**`allAuthenticatedUsers` = 任何登入 Google 帳號的人**

### IAM vs ACL

#### ACL（Access Control List，舊系統）

- 控制粒度：可以細到**單一 object**（單一檔案）
- 每個檔案自己帶一張權限清單
- 例如：`cat.jpg` 這個檔案，小明可讀、小華可寫

#### IAM（Identity and Access Management，新系統）

- 控制粒度：**整個 bucket**（這個層級以上）
- 跟 GCP 所有其他服務共用同一套系統

IAM用Role表達可以做的事

| 角色                            | 白話                |
| ----------------------------- | ----------------- |
| `roles/storage.objectViewer`  | 只能看和下載檔案          |
| `roles/storage.objectCreator` | 只能上傳，不能讀別人的       |
| `roles/storage.objectAdmin`   | 檔案的完整控制（讀寫刪）      |
| `roles/storage.admin`         | 連 bucket 本身的設定都能改 |

正常來說IAM跟ACL是聯集，所以一邊過就都過

解法：Uniform Bucket-Level Access

GCP 提供一個 bucket 設定叫 **Uniform bucket-level access**，開啟後：

- ACL **整個停用**，不管以前設了什麼都失效
- 只剩 IAM 一套系統生效
- 要稽核權限，只看一個地方