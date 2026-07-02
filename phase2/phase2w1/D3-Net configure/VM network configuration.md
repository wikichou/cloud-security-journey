今天的目標就是讓兩台VM用host only可以網路互通

![[network.png|697]]
這是現有的網路
![[VMconfig.png]]
進入VM，選擇機器->設定->網路，接著按照自己的需求配置網路
再來就可以進去嘗試互相ping
![[VM1 ip.png|645]]
![[VM2 ip.png|647]]
確認好兩台都有被分配的IP並且在同一個網段內
![[ping.png]]
最後就能看到IP確實可以ping通