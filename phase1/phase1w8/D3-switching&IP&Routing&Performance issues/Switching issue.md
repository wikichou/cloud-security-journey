### 注意不要產生loop
由於Mac frame不像是IP packet有TTL，有時frame會在switch之間形成迴圈，spanning tree protocol可以很好的做到這一點
switching，也就是bridge之間會不停的更新網路的拓樸，並且每一個STP port，也就是switch之間的連線也會有不同的狀態來防止這個狀況
- block
- listening
- learning
- forwarding
- disable

### VLAN assigning
實體介面跟VLAN之間要有正確的配置

### Access control
如果其他配置都是正確的但網路還是不通，那有可能就是access control沒有做好