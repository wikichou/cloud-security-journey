標準化的 device 管理介面協議

## 核心概念
- **MIB（Management Information Base）**：樹狀結構的資料庫「定義檔」，
  定義這台 device 有哪些可查詢的參數項目
- **OID（Object Identifier）**：MIB 樹上每個節點的唯一路徑編號，
  用來指定要查詢哪一個參數
- 查詢走 **UDP/161**（manager → device）

## 版本差異
| 版本 | 特點 |
|------|------|
| v1 | 結構化表格，**明碼傳輸** |
| v2c | 強化 data type，支援 bulk transfer，**仍明碼傳輸** |
| v3 | 加密 + 認證 + 資料完整性驗證（USM 機制） |

## SNMP Trap
> 🆕 新增：Trap 走 **UDP/162**（device → manager，方向相反）

Device **主動**推送事件通知給 manager，
解決 SNMP polling 機制無法及時發現突發事件的問題