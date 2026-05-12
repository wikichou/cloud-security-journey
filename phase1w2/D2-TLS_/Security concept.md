
傳輸本身並不確保安全，要加入額外的阻擋
ex. IPS, firewall or protocol like TLS, IPSec

public key infrastructure是用來管理公鑰或是憑證的

Digital certificate
->中央管理，由特定權威機構發行的CA做法，他發行的憑證大家信任
web trust
->去中心化，A信BB信C，所以A信C

CA:可信任的憑證簽署，用自己的私鑰替別人的憑證簽章證實他是真的

Identity and access management(IAM)
->保護資料，確認他可以被存取的範圍，並且記錄追蹤他的存取

TLS
->網路通訊的安全性協議，主要用於web application跟Server溝通
跟SSL差異是TLS是SSL的繼承者

TLS hand shake
->啟動TLS前的交握動作
1.雙方say hello, 協商通訊加密規格ex. TLS版本/加密演算法
2.server給出憑證證明身分
3.交換session key，這又分成幾個小步驟
(1)client用server的public 加密一個數值交給server
(2)server用private解開他
(3)利用這個數值推測一組對稱的key用於加密通訊
![[Pasted image 20260512223524.png]]
CA chain
因為root CA不能給所有人用，所以由root簽署幾張CA給一些權威單位，這些單位在簽署更多CA出去，如此一層一層的結構叫做CA chain