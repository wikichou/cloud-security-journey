Linux capabilities的本質就是把root能做到的事情拆分成不同的獨立能力，而當某個process/app需要用到對應的能力的時候只分配root等級的那個能力給他，而不是給他整個root權限

需要這個東西單純是為了資安考量，傳統的Unix模型只有兩種類型權限:root跟normal user，但在這個情境下就會衍生一個問題，假設說我今天想要用ping，ping要發ICMP封包需要raw socket的能力，傳統結構下因為沒有拆分功能所以我就得要給他整個root的權限，這導致攻擊者可以利用這點去取得不該有的權限，這嚴重的違反了最小權限。

**Linux capabilities 就是來解這個的**:把「root 能做的所有事」拆成幾十個獨立的細項能力(capability),每個程式只拿它真正需要的那幾項。

**每個 process 身上帶著一組 capability 的 bitmask**(一串 bit,每個 bit 代表「有沒有這項能力」)。kernel 做特權檢查時,不再問「你是不是 root」,而是問「你這串 bit 裡,對應這個操作的那一位是不是 1」。

因此，root在現代來說就是一個擁有全部capability的process
capability大致上可以這樣分

|Capability|能做什麼|危險度|
|---|---|---|
|`CAP_SYS_ADMIN`|一大堆系統管理操作(mount、改 namespace、改核心參數……)|🔴 **幾乎等同完整 root**,俗稱「新的 root」|
|`CAP_DAC_OVERRIDE`|繞過所有檔案讀寫權限檢查(無視 rwx)|🔴 極危險,能讀寫任何檔案|
|`CAP_SETUID`|任意改變 process 的 UID|🟠 危險,可提權變 root|
|`CAP_NET_ADMIN`|網路設定管理(改 IP、路由、防火牆規則)|🟠 網路層威脅大|
|`CAP_NET_RAW`|開 raw socket(送自訂封包,`ping` 就靠這個)|🟡 相對受限但仍需注意|
重點是 CAP_SYS_ADMIN幾乎就等於傳統意義上的root了，它涵蓋了大多數可操作的範圍，也就是說有了他幾乎等於拿到機器，所以在設定時要儘量避免他。

另外，一個process身上其實會帶有好幾組capability集合，他們有各自的用途

| 集合 | 白話意義 |
|---|---|
| **Permitted** | 這個 process「被允許持有」的能力上限（它最多能啟用哪些） |
| **Effective** | 「此刻實際生效」的能力（kernel 真正拿來檢查的就是這組） |
| **Bounding** | 一個天花板——限制這個 process 及其子孫**永遠不可能**取得哪些能力 |
| **Inheritable** | 執行新程式（execve）時可以傳遞下去的能力 |

日常理解抓住 **Permitted（我能有什麼）** 和 **Effective（我現在真的在用什麼）** 這兩個就夠了。**Bounding set** 之後在容器安全會重要——Docker 就是靠縮小 bounding set，確保容器內就算是 root 也永遠拿不到某些危險 capability。

### 總結
**capability = kernel 把「是不是 root」這個單一特權開關,拆解成幾十個獨立的布林旗標(bitmask)。每個 process 帶著這串旗標,kernel 檢查特權時查對應的位元而非查 UID。root 不過是「所有旗標都為 1」的 process。** 這讓「給程式剛好夠用的權限」變得可能——也就是最小權限原則的底層實作。

```
getcap /usr/bin/ping
```

![[get cap.png]]

```
getcap /usr/bin/ping
```
![[check ping cap.png]]