# Nmap 練習紀錄（2026-07-05）

環境：VirtualBox Host-only network，網段 192.168.56.0/24

## 1. 主機發現（Ping Scan）

```
nmap -sn 192.168.56.0/24
```

`-sn`：只做 Ping Scan（主機發現），不掃連接埠。用來確認網段內哪些主機是活著的，速度快，適合先掌握有哪些目標可以打。

![nmap -sn](nmap%20-sn.png)

- 掃描結果：4 台主機 up
  - 192.168.56.1（Host-only 閘道）
  - 192.168.56.100
  - 192.168.56.101（Oracle VirtualBox virtual NIC）
  - 192.168.56.102（Oracle VirtualBox virtual NIC）

## 2. TCP Connect Scan

```
nmap -sT 192.168.56.101
```

`-sT`：TCP Connect Scan，對每個埠完成完整的三次握手（SYN → SYN/ACK → ACK）來判斷埠是 open/closed/filtered。不需要 root 權限，但因為建立完整連線，比較容易被目標的 log 記錄下來。

![nmap -sT](nmap%20-sT.png)

- 目標：192.168.56.101
- 結果：
  - 22/tcp open ssh
  - 443/tcp closed https
  - 其餘 998 埠 filtered（no-response）

## 3. 服務版本偵測（Version Detection）

```
nmap -sV 192.168.56.101
```

`-sV`：在確認埠是 open 之後，進一步偵測該埠上跑的服務名稱、版本號，並嘗試推測作業系統。用來判斷目標軟體是否有已知漏洞（例如特定版本的 OpenSSH）。

![nmap -sV](nmap%20-sV.png)

- 22/tcp open ssh → **OpenSSH 8.9p1 Ubuntu 3ubuntu0.15**（Ubuntu Linux, protocol 2.0）
- OS 判斷：Linux, cpe:/o:linux:linux_kernel

## 4. ARP table

```
ip neigh
```

確認目前的ARP table

![[ip neigh.png]]

101就是另一台機器

## 5. Layer 7 服務測試（HTTP Server）

### Server 端

```
python3 -m http.server 8000
```

在 192.168.56.101 上開一個簡易 HTTP 服務，監聽 8000 port，用來當作 Layer 7 的測試目標。

![[L7 server.png]]

- log 顯示 192.168.56.102 有連進來要求 `GET /`，回應 200

### Client 端

```
curl http://192.168.56.101:8000
```

從 client 端對 8000 port 發送 HTTP 請求，測試 Layer 7 應用層是否能正常溝通。

![[L7 client.png]]

- 回應為 Python http.server 預設的 `Directory listing for /` 頁面，代表連線與服務都正常

## 6. UFW 防火牆規則測試（Deny Port 8000）

### Server 端（設定防火牆規則）

```
sudo ufw status
```

在 server（192.168.56.101）上用 ufw 設定規則，把 8000 port 擋掉（deny），其餘服務維持開放。

![[server deny.png]]

- 22/tcp、443/tcp：allow anywhere
- 22：只允許來自 192.168.1.0/24
- 8000：deny anywhere（含 v6）

### Client 端（連線被擋）

```
curl http://192.168.56.101:8000
```

規則生效後，client 再次對 8000 port 發送請求，驗證 ufw 的 deny 規則是否確實擋下流量。

![[client deny.png]]

- 對照第 5 節同樣的指令，這次因為 ufw deny 而沒有回應，確認防火牆規則生效

