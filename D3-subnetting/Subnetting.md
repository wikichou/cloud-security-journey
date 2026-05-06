VLSM(virtual length subnet mask)
自訂子網路遮罩來切出剛好的host數量

ex.我需要50台主機，我的router IP是192.168.2.1

用CIDR推出可以切幾個子網路，找出該IP落在哪一段:subnet address
找出這一段最後一個:broadcast

ex. 10.1.1.224/22

22-16 = 6 子網路有2^6組(0,4,8......) 1落在0~4之間
->subnet address: 10.1.0.0
broadcast:10.3.255
host range 10.1.0.1~10.1.3.254