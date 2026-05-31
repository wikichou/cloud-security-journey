要含字串的時候要用*
不確定怎麼做的時候可以用Get-help

# 列出所有可用指令
Get-Command

# 搜尋含特定關鍵字的指令
Get-Command *network*
Get-Command *process*

# 查指令說明文件
Get-Help Get-Process
Get-Help Get-Service

# 查執行中的程序
Get-Process

# 查系統服務狀態
Get-Service

# 查 TCP 連線（類似 netstat -ano）
Get-NetTCPConnection

# 查網卡資訊
Get-NetIPAddress

# 查路由表
Get-NetRoute

# 找記憶體用量前 5 名的程序
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5

# 只看正在執行的服務
Get-Service | Where-Object { $_.Status -eq "Running" }

# 只看 ESTABLISHED 的連線
Get-NetTCPConnection | Where-Object { $_.State -eq "Established" }