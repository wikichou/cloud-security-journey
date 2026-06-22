ipconfig /all
->完整網卡資訊

netstat -an
->查看所有TCP/UDP狀態(-a 全部 -n 不解析主機名 -o 看哪個PID占用哪個port)
->看完之後可以配合tasklist | findstr[pid] 來看是哪個process在連線，可以做一個基本調查

tracert 
->追蹤封包路由(windows的traceroute)

systeminfo
->系統資訊:OS 版本,補丁,硬體

tasklist
->看執行中的process(約等於linux ps aux)

arp -a
->看誰在我的區網內

route print
->看路由表

netsh advfirewall show allprofiles
->netsh 看防火牆設定

netsh wlan show profiles
->看wifi profiles