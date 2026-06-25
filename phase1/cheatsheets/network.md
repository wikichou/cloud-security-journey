## OSI 七層
| 層   | 名稱           | 功能          | 對應協議            |
| --- | ------------ | ----------- | --------------- |
| 7   | Application  | 使用者介面       | HTTP, DNS, SMTP |
| 6   | Presentation | 加解密, 壓縮     | TLS,SSL         |
| 5   | Session      | 管理連線        | RPC             |
| 4   | Transport    | 端到端連線，流量控制  | TCP, UDP        |
| 3   | Network      | routing, IP | IP              |
| 2   | Data link    | MAC,        | Ethernet        |
| 1   | Physical     | 硬體傳輸        | cable           |
...

## TCP vs UDP
|      | TCP       | UDP           |
| ---- | --------- | ------------- |
| 連線   | 三次握手      | 無連線           |
| 可靠性  | 可保證, 重傳   | 無法保證, 不重傳     |
| 速度   | 慢         | 快             |
| 應用場景 | HTTP, SSH | 串流, DNS, DHCP |
...

## 常見 Port 號
| Port | 協議     | 備註           |
| ---- | ------ | ------------ |
| 21   | FTP    | 檔案傳輸         |
| 22   | SSH    |              |
| 23   | Telnet | 不加密，已棄用      |
| 25   | SMTP   | 寄信           |
| 53   | DNS    | TCP+UDP      |
| 80   | HTTP   |              |
| 110  | POP3   | 收信           |
| 143  | IMAP   | 收信（支援多裝置同步）  |
| 443  | HTTPS  |              |
| 445  | SMB    | Windows 檔案共享 |
| 3389 | RDP    | 遠端桌面         |
...

## Wireshark 常用 filter
| filter                               | 用途                   |
| ------------------------------------ | -------------------- |
| tcp                                  | 只看 TCP               |
| dns                                  | 只看 DNS 查詢            |
| http                                 | 只看 HTTP              |
| tcp.flags.syn==1                     | 只看 SYN 封包            |
| tcp.flags.syn==1 && tcp.flags.ack==0 | 只看初始 SYN（排除 SYN-ACK） |
| ip.addr==192.168.x.x                 | 篩選特定 IP 的所有流量        |
...
## DNS 記錄類型

| 記錄類型 | 用途 |
|---|---|
| A | 網域 → IPv4 |
| AAAA | 網域 → IPv6 |
| CNAME | 網域別名 |
| MX | 郵件伺服器 |
| NS | 權威名稱伺服器 |
| TXT | 驗證、SPF、DKIM |
## 常見網路攻擊類型

| 攻擊 | 目標層 | 原理 |
|---|---|---|
| ARP Poisoning | Layer 2 | 偽造 ARP 回應，污染 ARP cache，攔截流量 |
| DNS Poisoning | Layer 7 | 偽造 DNS 回應，導向惡意 IP |
| VLAN Hopping | Layer 2 | 偽造 trunk 封包跨越 VLAN 隔離 |
| MAC Flooding | Layer 2 | 塞爆 switch 的 MAC table，使其退化成 hub |
| DDoS | Layer 3/4 | 大量流量癱瘓目標服務 |