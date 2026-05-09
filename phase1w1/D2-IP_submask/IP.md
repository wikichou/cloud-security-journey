# IPv4 位址與子網路基礎

IP 是一個裝置在網路上的位置識別碼。

## 重要名詞

| 名詞 | 說明 |
|------|------|
| 子網路遮罩（Subnet Mask） | 用來區分 IP 的 Network 段與 Host 段 |
| Default Gateway | 網段內用來向外傳輸的 IP，通常指派給 Router |
| Loopback Address | 自己連自己的位址（127.0.0.1） |
| VIP（Virtual IP） | 由軟體層面管理的 IP，不綁定在特定網卡上 |

## IP 指派方式

- **手動配置**：早期作法，現已少用
- **DHCP**：自動指派 IP 及其他網路設定
- **APIPA（Automatic Private IP Addressing）**：無 DHCP 時的備援機制，範圍 `169.254.0.0/16`，僅限同一網段內使用，無法經過 Router

## Classful IP 等級（已淘汰）

| 等級 | 第一個 Octet 範圍 | 用途 |
|------|------------------|------|
| Class A | 0 – 127 | 大型網路 |
| Class B | 128 – 191 | 中型網路 |
| Class C | 192 – 223 | 小型網路 |
| Class D | 224 – 239 | Multicast |
| Class E | 240 – 255 | 保留 |

> 現代已改用 **CIDR**（Classless Inter-Domain Routing），以斜線表示遮罩長度，例如 `255.255.128.0 = /17`

## Private IP 與 NAT

因為 IPv4 位址不足，出現 Private IP 的概念：
- Private IP 不能直接用於 Routing
- 透過 **NAT（Network Address Translation）** 將 Private IP 轉換為 Public IP 與外界溝通

## 子網路的四個關鍵位址

| 位址 | 說明 |
|------|------|
| Network Address | 第一個位址，Host 全為 0 |
| First Usable Address | Network + 1 |
| Last Usable Address | Broadcast - 1 |
| Broadcast Address | 最後一個位址，Host 全為 1 |
