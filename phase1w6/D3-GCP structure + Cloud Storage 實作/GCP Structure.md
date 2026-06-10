![[GCP Structure.png]]每一層以公司舉例的話大概像這樣
Organization（公司）
    └── Folder（部門）
            └── Project（專案/產品）
                    └── Resource（實際的東西）



**Organization — 公司**

- 整個 GCP 帳號的最頂層
- 通常對應一個企業的 Google Workspace 網域（例如 `yourcompany.com`）
- 個人帳號（Gmail）沒有 Organization，直接從 Project 開始
- 在這層設定的 Policy 會往下繼承到所有 Folder 和 Project

**Folder — 部門**

- 用來把 Project 分組的容器
- 例如：`研發部門 Folder` 下有 `前端 Project`、`後端 Project`、`資安 Project`
- 可以多層巢狀：部門 → 子部門 → Project

**Project — 你現在用的這層**
- GCP 裡**最核心的隔離單位**
- `gcp-security-lab` 就是一個 Project
- 所有資源都必須屬於某個 Project
- 計費也是以 Project 為單位
- IAM 權限設定通常在這層

**Resource — 實際的雲端資源**

- 這才是真正用的東西
- 例如：一台 VM、一個 Storage Bucket、一條 Firewall Rule、一個 Service Account
- 每個 Resource 都屬於某個 Project