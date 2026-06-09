
## 雲端的優勢
1.容易布署
2.高彈性
3.好擴充
4.架構可以直接複用

## Virtual Network>NFV(Network function virtualization)
把網路設備都虛擬化，並且用hypervisor管理他們

## VPC(Virtual private cloud)
放在公共雲上面的資源pool，大型環境中可以用來單獨處理單一部門/app的需求，不同的VPC之間用transit gateway連線，也就是一個虛擬的router

VPC本身也可以有一個gate way來讓使用者用internet連線，或是說用NAT去存取網路資源，也可以用EndPoint做cloud to cloud的直連
同樣的也可以加入security list，但是這個list會被分配給所有的private cloud導致設定不夠細緻，所以可以加入groud來方便管理