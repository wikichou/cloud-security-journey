OSI:敘述資料傳輸的概覽，並且可以與主流的TCP/IP相容
OSI由上至下
1.應用:application
2.呈現:presention
3.會話:session
4.傳輸:transport
5.網路:network
6.資料連結:datalink
7.實體:physic

L1:實際硬體
L2:乙太網路, MAC,交話
L3:routing, IP, packet
L4:實際傳輸內容
L5控制/通訊協定,作為L4跟L6的連結
L6:呈現,加解密,SSL/TLS
L7:使用者互動

可以使用wireshark抓出來看