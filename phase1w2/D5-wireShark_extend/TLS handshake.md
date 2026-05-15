![[螢幕擷取畫面 2026-05-15 212415.png]]
前三筆就是handshake的過程
client hello -> server hello > client response ,完成hand shake![[螢幕擷取畫面 2026-05-15 212639.png]]
這裡有四個地方可以關注一下
1.這個是TLS1.3的封包，但為了向下相容所以會寫1.2
2.這裡才是標註了使用1.3
3.這邊是實際完成握手後加密的傳輸資料
4.TLS的(指紋)，依照server hello的cipher suite, TLS版本等等產生的，可以用來識別特定的server或是流量