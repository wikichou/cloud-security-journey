接續昨天的縮小攻擊面的防護手法，今天要做的事情是處理capablilty，先複習何謂capability，傳統的linux的root權限只有全有或是全無，這件事情太危險了，所以capability就是把root的權限拆成幾十個細項，這些細項就是capability。
ex.
- `CAP_NET_BIND_SERVICE` — 允許綁定 1024 以下的低號 port(如 80、443)
- `CAP_NET_RAW` — 允許送 raw socket(ping 靠這個)
- `CAP_SYS_ADMIN` — 幾乎等同 root
昨天的「非 root」是降低使用者層級的權限。今天的 capability 是**另一個維度** —— 就算你是 root,也可以只給你需要的那幾項 capability,把其他危險的全拿掉。兩者疊加才是完整的最小權限。

### runtime flag

```
docker run --cap-drop ALL --cap-add NET_BIND_SERVICE `
  --read-only --tmpfs /tmp `
  --security-opt no-new-privileges `
  three-tier-app-test
```

(PowerShell 換行用反引號 `` ` ``,不是 Linux 的反斜線 `\`,這點在 Windows 上要注意)

- --cap-drop ALL --cap-add NET_BIND_SERVICE(最小權限)
	這段在做的事情是先把所有的capability砍掉，再把需要的加回來，以此達到所謂的最小權限，這種白名單式的作法才是資安的正確思維，**預設全部拒絕(deny by default),再明確允許需要的**。

- `--read-only --tmpfs /tmp`(唯讀檔案系統)
	這裡在做的事情是把整個container都設成為唯讀，這樣即便被攻擊者進來了，他也沒辦法寫入任何檔案，所以惡意程式下載，設定檔修改等等手段都無法實行。
	這麼做有個問題，很多程式都需要寫暫存檔，所以要在tmp底下掛一個記憶體暫存區，也就是tmps
	`tmpfs` 是掛在**記憶體**裡的暫存檔案系統,container 一關掉裡面東西就消失。這樣既保住「主要檔案系統唯讀」的防禦,又給程式一個能寫暫存的地方。這就是資安裡常見的「最小化例外」—— 不是為了方便就整個開放,而是精準地只開必要的那一小塊。
- `--security-opt no-new-privileges`(禁止晉升)
	no-new-privileges會禁止container裡面的process透過setuid之類的機制取得比啟動的時候更高的權限。
	Linux 有些執行檔帶 **setuid bit**,執行時會用檔案擁有者(常是 root)的權限跑,而不是執行者的權限。攻擊者常利用這種檔案來提權(privilege escalation)。加了 `no-new-privileges`,就算容器裡有這種檔案,也無法藉此變成 root。
	這一項直接呼應昨天做的「非 root」—— 昨天讓你不是 root,今天這個 flag 確保你**沒辦法偷偷變回 root**。兩個是配套的。


![[touch file.png]]
![[capability.png]]
