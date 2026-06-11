
## SDN(Software defined network)

將原先網路硬體設備的功能寫成軟體，部屬上會方便許多
分層為
-infrastructure layer/data plane
實際流量通過跟操作流量本身的地方，也就是硬體裝置上的插孔
-Control layer/Control plane
決定data plane行為的地方，例如說NAT table等，對應的是硬體的內部處理
-Application layer/Management plane
操作，設定device本身的地方，像是SSH這種，對應的是硬體的控制面板

### SD-WAN
->在cloud上建立的WAN，服務不再集中於data center，利用Zero touch provising，WAN中的服務可以自我配置，即便服務變更了也不用人力介入

## Zero trust
原本資安的作法上一但某個實體進入了網路內部後，防範機制就會大幅度減少，Zero trust就是為了解決這個問題，這個做法上不信任任何實體，包含使用者、流量、裝置...以此加強防範

### Policy based authentication
Adaptive identity ->除了基本的帳密之外，依照使用者的位置，身分，連線方式等等去決定他目前的身分以及是否需要額外的驗證方式，以達到不同的身分可以有著不同的權限

### Secure Access Service Edge(SASE)
下一代的VPN，無論服務在雲上，在datacenter或是使用者是在哪用什麼都會經過這個edge，可以在這裡面強化保護措施，必須要在使用者端安裝client