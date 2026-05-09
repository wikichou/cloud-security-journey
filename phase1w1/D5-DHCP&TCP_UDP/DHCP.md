# DHCP（Dynamic Host Configuration Protocol）

DHCP 用來自動為裝置指派 IP 及相關網路設定，前身為 Bootstrap Protocol（BOOTP）。

## DORA 流程（取得 IP 的四步驟）

```
Host (0.0.0.0)                        DHCP Server
     |                                      |
     |--- 1. Discover (UDP/68 → Broadcast) ->|  「我需要一個 IP」
     |                                      |
     |<-- 2. Offer   (UDP/67 → Broadcast) --|  「我可以給你這個 IP」
     |                                      |
     |--- 3. Request (UDP/68 → Broadcast) ->|  「我選擇用你的 IP」
     |                                      |
     |<-- 4. ACK     (UDP/67 → Broadcast) --|  「確認，IP 已指派給你」
```

> 網段內可能有多台 DHCP Server 同時回應 Offer，Host 選定一台後，用 Request 廣播告知所有 Server 決定結果。

## DHCP Relay（跨網段）

DHCP 本身只能在同一網段內運作，無法穿越 Router。需要跨網段時，可透過 **DHCP Relay** 解決：

- Router 收到 Discover 封包後，以 **Unicast** 轉發給遠端 DHCP Server
- 後續回傳也由 Router 以 Unicast 代為轉送
- 流程同樣是 DORA，對 Host 來說行為透明

## DHCP Server 配置項目

| 設定項目 | 說明 |
|----------|------|
| DHCP Scope | 可指派的 IP 範圍 |
| Subnet Mask | 子網路遮罩 |
| Lease Duration | IP 的租用時長，到期後 Server 回收 |
| DNS Server | 指定 DNS Server 位址 |
| Default Gateway | 指定預設閘道 |

## IP 保留與 MAC 綁定

- DHCP Server 會儘量讓相同 MAC Address 的裝置取得相同的 IP
- 可設定「保留 IP（Reservation）」，讓特定 MAC Address 永遠拿到固定的 IP

## Lease 更新計時器

IP 不會等到完全到期才更新，有兩個計時器提前觸發：

| 計時器 | 觸發時機 | 行為 |
|--------|----------|------|
| T1 | Lease 時間的 50% | 向原 DHCP Server 請求續租 |
| T2 | Lease 時間的 85% | 若 T1 失敗，向任意 DHCP Server 廣播請求 |
