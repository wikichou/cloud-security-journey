
 $conn = Get-NetTCPConnection | Where-Object { $_.State -eq "Established" }
>> $conn | ForEach-Object {
>>     $proc = Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue
>>     [PSCustomObject]@{
>>         LocalPort  = $_.LocalPort
>>         RemoteAddress = $_.RemoteAddress
>>         RemotePort = $_.RemotePort
>>         ProcessName = $proc.Name
>>     }
>> }


這段內容比較特別
# 第一步：把已經建立好連線的結果存進變數
$conn = Get-NetTCPConnection | Where-Object { $_.State -eq "Established" }
# 第二步：逐筆處理
$conn | ForEach-Object {
# 用 PID 查程式名稱
    $proc = Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue
    # 組合成自訂輸出格式
    [PSCustomObject]@{
        LocalPort     = $_.LocalPort
        RemoteAddress = $_.RemoteAddress
        RemotePort    = $_.RemotePort
        ProcessName   = $proc.Name
    }