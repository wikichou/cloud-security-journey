# Network Solutions — 網路監控與管理

---

## 一、收集網路資訊的方法

| 工具 | 說明 |
|------|------|
| **LLDP / CDP** | Layer 2 協定，自動發現鄰近網路設備（拓撲圖）；CDP 是 Cisco 私有，LLDP 是開放標準 |
| **IP Scanner** | 掃描活躍主機與開放 Port（如 nmap、Angry IP Scanner） |
| **Commercial Scanner** | Nessus、Qualys 等，掃描漏洞並產生合規報告 |
| **SNMP** | 向網路設備查詢 OID 取得設備資訊、狀態、介面統計；v3 才有加密與認證 |

> 收集到的資料整理後可進行 **Traffic Analysis（流量分析）**，建立正常基準線，偵測異常行為。

---

## 二、收集硬體 / 流量資訊的方法

| 工具 | 說明 |
|------|------|
| **SNMP** | 取得 CPU、記憶體、介面狀態等硬體資訊 |
| **NetFlow / IPFIX / sFlow** | 流量摘要資料（誰跟誰通、用多少頻寬），不包含封包內容；NetFlow 是 Cisco 格式，IPFIX 是標準化版本，sFlow 是隨機取樣版本 |
| **Protocol Analysis（封包分析）** | Wireshark、tcpdump 等，擷取完整封包內容，用於深度診斷 |
| **Software Agent** | 安裝在主機上的代理程式，回報硬體清單、OS 版本、執行中服務等 |

---

## 三、雲端環境特有的 Network Solutions

| 工具 | 平台 | 說明 |
|------|------|------|
| **VPC Flow Logs** | AWS / GCP / Azure | 記錄進出 VPC 的 IP 流量（來源、目標、Port、允許/拒絕） |
| **AWS Network Firewall** | AWS | 受管的 Stateful 防火牆，可設定 IDS/IPS 規則 |
| **GCP Cloud Armor** | GCP | WAF + DDoS 防護，可針對 Layer 7 威脅過濾 |
| **Azure Network Watcher** | Azure | 封包擷取、連線診斷、拓撲視覺化 |
| **Private Link / VPC Peering** | 跨雲通用 | 讓服務在私有網路內通訊，避免流量走公網 |

---

## 四、IDS / IPS

- **IDS（Intrusion Detection System）**：偵測異常流量，**只告警不攔截**
- **IPS（Intrusion Prevention System）**：偵測後**主動攔截**惡意流量
- 部署位置：通常放在防火牆後方、關鍵網段前
- 雲端中通常整合在 WAF 或 Network Firewall 內

---

## 五、Availability 監測

- **監測目標**：Link 狀態、設備回應（ICMP Ping）、服務健康（HTTP Health Check）
- **工具**：SNMP Trap、Prometheus + Alertmanager、CloudWatch / Stackdriver
- **目標**：及早偵測中斷，配合 SLA/SLO 的 Uptime 要求

---

## 六、Change Management — 保留舊版 Config

**為什麼重要：**
- 設定錯誤是網路中斷最常見原因之一
- 防火牆或路由器 config 更動後若發生問題，需快速 rollback

**最佳實踐：**
1. 所有 config 更動前先備份（版本控制，如 git 或 RANCID/Oxidized）
2. 記錄變更原因、時間、執行者（Change Log）
3. 測試環境先驗證，再部署到 Production
4. 保留至少最近 N 個版本，可快速還原

---

## 七、Network Baseline 基準線

- 記錄正常狀態下的：頻寬使用量、連線數、常見協定比例、Top Talkers
- 偏離基準線 → 觸發告警（可能是攻擊、設備異常、配置錯誤）
- 工具：NetFlow Analyzer、ELK Stack、SIEM（如 Splunk）

---

## 關鍵觀念整理

```
Discovery  →  Baseline  →  Monitor  →  Alert  →  Respond  →  Change Mgmt
（發現資產）  （建基準）  （持續監測）（異常告警）（事件回應）（記錄變更）
```
