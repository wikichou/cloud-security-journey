# DNS（Domain Name System）

DNS 負責查詢 Domain Name 與 IP 的對應關係。

## 基本概念

- **DNS Database**：採階層式（Hierarchy）結構
- **Primary DNS Server**：負責儲存與更新 DNS 記錄
- **Secondary DNS Server**：唯讀，用於負載分散與備援
- **Local Name Resolution**：不透過 DNS，直接用本機 `hosts` 檔案對應 IP 與 Domain Name

## 查詢類型

| 查詢 | 說明 |
|------|------|
| Lookup（正向查詢） | 給 Domain Name，回傳 IP |
| Reverse Lookup（反向查詢） | 給 IP，回傳 Domain Name |

## DNS Server 種類

| 類型 | 說明 |
|------|------|
| Authoritative DNS Server | 儲存原始 DNS 對應記錄的來源 |
| Non-Authoritative DNS Server | 只有 Cache，無原始記錄 |

Cache 資訊透過 **TTL（Time To Live）** 判斷是否過期，過期後重新查詢。

## 遞迴查詢流程（Recursive DNS Query）

以查詢 `www.test.com` 為例：

```
Client
  └─> Root Server（查 .）
        └─> .com Server（查 .com）
              └─> test.com Name Server（查 www.test.com）
                    └─> 回傳 IP → Cache 在本地 DNS Server
```

**工具**：`dig` 指令可用來執行 DNS 查詢

## DNS 安全

| 機制 | 說明 |
|------|------|
| DNSSEC | 對 DNS 記錄進行簽章（Signed），防止偽造 |
| DNS over TLS | 用 TLS 加密 DNS 查詢流量 |
| DNS over HTTPS | 用 HTTPS 加密 DNS 查詢流量 |

## DNS Record 類型

| Record 類型 | 說明 |
|-------------|------|
| SOA（Start of Authority） | 總攬，記錄此 Zone 的基本資訊 |
| A | Domain → IPv4 |
| AAAA | Domain → IPv6 |
| CNAME（Canonical Name） | 一個 Domain Name 指向另一個 Domain Name（別名 → 正式名稱） |
| MX（Mail Exchange） | 記錄負責收信的 Mail Server hostname |
| TXT | 存放文字資料，常用於 SPF / DKIM 等 Email 驗證 |
| NS（Name Server） | 指向此 Domain 的 Name Server |
| PTR（Pointer） | 用於 Reverse Lookup，IP → Domain |
