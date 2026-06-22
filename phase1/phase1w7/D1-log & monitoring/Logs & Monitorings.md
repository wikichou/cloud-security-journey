
## Logging
記錄所有發生的事情，並且及時監控特定事件

## NetFlow
網路流量的統計工具，可以用探針（probe）蒐集資訊傳送到蒐集中心（collector）
> ⚠️ 修正：NetFlow 記錄的是 flow 的 **metadata**（來源/目的 IP、Port、
> 封包數量、傳輸量），**不是封包內容本身**，這點和 protocol analyzer 不同

## Protocol Analyzer
直接看封包內容的工具，ex. Wireshark

## Network Baseline
利用統計歸納出的一組正常流量標準，可以用來判斷 server 或 device
的流量是否異常（超出 baseline = 值得調查的事件）

## Syslog
Log 的一種標準格式，會被傳輸到 SIEM 做儲存，SIEM 本身也有
dashboard 和 alert system
> 🆕 新增：Syslog 有 8 個 severity level（數字越小越嚴重）：
> | Level | 名稱 | 說明 |
> |-------|------|------|
> | 0 | Emergency | 系統無法使用 |
> | 1 | Alert | 需要立即處理 |
> | 2 | Critical | 嚴重錯誤 |
> | 3 | Error | 一般錯誤 |
> | 4 | Warning | 警告 |
> | 5 | Notice | 正常但值得注意 |
> | 6 | Informational | 一般資訊 |
> | 7 | Debug | 除錯用 |

## API Integration
統一用 API 管理大量 devices

## Port Mirroring / SPAN
> ⚠️ 術語修正：你描述的行為正式名稱是 **Port Mirroring** 或
> **SPAN（Switched Port Analyzer）**
把通過 switch 特定 port 的流量用鏡像方式複製一份紀錄
跨 switch 鏡像的版本叫做 **RSPAN（Remote SPAN）**，
適合在 data center 集中管理監控流量