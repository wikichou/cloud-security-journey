
這些封包內可以看出來他們的Syn跟Ack的號碼確實有關連，syn的sequence會被syn-ack拿去做ack number且等於sequence number+1，往後也是，這樣確保了三次交握的可靠性，另外特別提一下syn包也會有ack number是因為TCP的Header是固定的，但可以看出來他仍然是0，沒有用上

-sS:送出sync收到sync-ack就結束，不建立連線
-sT:建立完整連線

Syn![[螢幕擷取畫面 2026-05-14 215913.png]]
Syn-Ack
![[螢幕擷取畫面 2026-05-14 220014.png]]
Ack![[螢幕擷取畫面 2026-05-14 220124.png]]
