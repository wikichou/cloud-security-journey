查詢domain name跟IP的關係

DNS datatbase: hireachy

通常會用好幾個DNS server，分成primary跟secondary
primary用來儲存跟更新，secondary用來讀而已

另外也可以不用DNS，local name resolution:做一個host file對應IP跟domain name

look ups:給name 回IP
reverse look up:給IP 回name

dig指令: DNS查詢工具

authority DNS server:用來存原始DNS對應表
no authority DNS:只有caching的
caching的資訊會用TTL來確認過期了沒，過期就更新

recursive DNS queries:遞迴的查詢，例如說www.test.com，會先去查.也就是root server, root server會告訴我.com存在哪裡，再去.com server查告訴我www.test.com存在哪，再去看www.test.com的IP，最後在caching在我的DNS server上

DNS本身不算安全，所以要有DNSSEC domain name security extention做signed
或著是加密可以用DNS over TLS或DNS over HTTPs

DNS records是DNS server儲存資訊的type，會有很多種
SOA:總攬
Address records:分成IPV4的(A)跟IPV6的(AAAA)
Canonical name records(CName):IP對多個name的紀錄
Mail exchange record(MX):存mail的 host name
Text record:存文字的，可以存SPF protocol或是domain keys，用來sign email的
name server record: 我的domain的name server
Pointer record:做 reverse look up的