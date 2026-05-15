![[螢幕擷取畫面 2026-05-15 213700.png]]
紅色的部分是DNS查詢，綠色是TCP三次交握，橘色則是四次揮手

另外備註一下，QUIC是google新開發得協議，建立在UDP之上
根據cloude
**QUIC 是用來取代 TCP + TLS 的新傳輸協議**，建立在 UDP 上
**為什麼要取代 TCP？**

TCP 有幾個老問題：

**1. 連線建立太慢** TCP 三次握手 + TLS Handshake，至少要 2-3 個來回才能開始傳資料。QUIC 把這兩件事合併，第一次連線 1-RTT，之後再連同一個 Server 甚至 0-RTT 直接傳資料。

**2. Head-of-line Blocking** TCP 是嚴格有序的，一個封包掉了，後面所有封包都要等它重傳。QUIC 在一條連線裡跑多個獨立的 stream，一個 stream 掉包不影響其他 stream。

**3. 換網路要重新連線** 你從 Wi-Fi 切到行動網路，IP 換了，TCP 連線就斷了要重建。QUIC 用 Connection ID 識別連線，IP 換了連線還在，手機用戶體感很明顯。

---

**QUIC 和你學過的東西的關係**

```
舊架構：HTTP/2 → TLS → TCP → IP
新架構：HTTP/3 → QUIC → UDP → IP
```

QUIC 內建加密（相當於 TLS 1.3），所以你在 Wireshark 看到的 QUIC 封包內容全部是 `Protected Payload`，跟 TLS Application Data 一樣看不到明文。

---

**為什麼跑在 UDP 上？**

UDP 沒有 TCP 那些內建機制（重傳、排序、流量控制），QUIC 自己在應用層重新實作這些功能，但可以做得更靈活、更有效率，不受作業系統 TCP 實作的限制。