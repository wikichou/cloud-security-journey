AKA spoofing，也就是偽造自己的身分
常常用在on path attack

ex.
ARP poisoning(IP spoofing)
->利用ARP廣播的取得連線對象MAC的做法，我把我自己偽造成他要連線的對象，讓他的ARP cache存我的MAC以此達到Man in the Middle攻擊

DNS spoofing
**方法一：改 DNS Server 的 config**（需要入侵 DNS Server）

```
直接進去改 DNS Server 上的記錄
google.com → 攻擊者的 IP
之後所有人查詢都拿到假資料
```

難度最高，需要先拿到 DNS Server 的存取權限。

**方法二：改受害者本機的 hosts 檔案**（不需要碰 DNS Server）

```
Windows: C:\Windows\System32\drivers\etc\hosts
Linux:   /etc/hosts
```

hosts 檔案的優先權比 DNS 還高，電腦查詢時先看 hosts，再去問 DNS。只要能改這個檔案，完全不需要碰 DNS Server。

**方法三：On-path Attack 攔截 DNS 回應**（不需要碰 DNS Server）

```
攻擊者先用 ARP Poisoning 插進中間
    ↓
受害者的 DNS 查詢經過攻擊者
    ↓
攻擊者在回應到達受害者之前竄改內容
    ↓
受害者收到假的 IP，DNS Server 完全不知道發生了什麼
```