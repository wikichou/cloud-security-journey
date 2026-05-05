
IP指的是一個裝置在網路上的位置，其中有許多重要名詞:
子網路遮罩:用來分辨裝置IP的network段跟Host段
default gate way:網段內用來向外傳輸的IP address，通常是給router
loopback address:自己連自己的Address
VIP:虛擬IP，由軟體層面管理的IP，不綁在特定的網卡上

過往IP都要手動處理，但現代問題有現代解決方案
DHCP:自動指派IP以及其他相關網路設定的協定
另外要是沒有建立DHCP的話，本地端內的網路也可以依靠automatic private IP addressing來指派IP，但是這個IP只有自己網段內可以使用，沒辦法經過router連到外面，範圍是169.254.0.0/16

因為IPV4不夠用了，所以開始有所謂private IP address的概念出現，這些IP是不能用於routing的，但是可以用NAT把private轉public與外界溝通

IPV4常見有三種等級的IP 位址等級
A/B/C
以及比較特別的D跟E
class A代表0~127
class B代表128~191
class C代表192~223
這裡指的是IP的第一組值的範圍
但基本上classful已經沒人用了

子網路切分上有幾個重要內容
network address
第一個子網路，也就是host全0

first usable address
network+1

broadcast address
最後一個子網路，也就是host全1

last usable address
broadcast-1

現代作法更多是用CIDR(Classes Inter-Domain Routing)
也就是用斜線多少的方式表示子網路遮罩
ex. 255.255.128.0 = /17