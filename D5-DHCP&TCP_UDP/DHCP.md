DHCP 是用來自動給裝置IP配置用的，早期用的叫做bootStrap protocol，後來改成dynamic host configuration protocol

host要IP的方式有四步:DORA

1.discover:host因為還沒有IP，所以用0.0.0.0:UDP/68送到broadcast找DHCP server
2.offer:DHCP server收到後用UDP/67送到broadcast找到要IP的host告訴她我可以給一組IP
3.request:因為網路內可能有多台DHCP server，所以可能收到好幾個offer，host挑好一個後再用0.0.0.:UDP/68到broadcast說我決定用誰的IP
4.Ack:DHCP再用UDP/67回傳給broadcast確認接收到request

因為先天的限制，DHCP只能走IPV4且只能在同一個網段內，出不了router，所以需要一些額外的幫助，例如說可以用router做DHCP relay(router會知道DHCP server的IP)
作法上也是DORA，只是當今天discover的時候router收到這個packet就會用unicast的方式丟給其他地方的DHCP server，後續router接回來也是unicast

DHCP server本身有一些東西要配置
DHCP scope:IP的range也就是可用的IP
subnet mask
lease duration: IP可用的時長，超過了DHCP server會回收
還有很多其他的設定可以設置:DNS server, default gateway...

DHCP server會儘量讓一樣的MAC address收到一樣的IP
並且可以加入保留的IP，讓這些IP只讓特定的裝置使用

lease time不會等到完全過期了才更新，會有兩個timer
T1:50% default lease time
T2:85% lease time