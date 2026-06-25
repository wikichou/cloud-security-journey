## Nmap Scan 類型

| 指令 | 類型 | 封包行為 | 需要 root |
|---|---|---|---|
| `-sT` | TCP connect | 完整三次握手 | 否 |
| `-sS` | SYN scan | SYN → SYN-ACK → RST | 是 |
| `-sU` | UDP scan | 送 UDP 封包 | 是 |
| `-sV` | Version detection | 額外探測 service 版本 | 否 |
| `-O` | OS detection | TTL 和封包特徵推測 OS | 是 |

## gcloud 常用指令

| 指令 | 用途 |
|---|---|
| `gcloud projects list` | 列出所有專案 |
| `gcloud services list --enabled` | 列出已啟用的 API |
| `gcloud services list --available \| grep -i security` | 搜尋安全相關 API |
| `gcloud logging read --limit=20` | 讀取最近 20 筆 log |
| `gcloud config configurations list` | 列出所有設定檔 |
| `gcloud auth list` | 查看目前登入帳號 |
| `gcloud config get-value project` | 查看目前專案 |