VirtualBox 給每張虛擬網卡（Network Adapter）配置一種模式，決定這台 VM 能跟誰說話：

**1. NAT（預設模式）**  
VM 透過 host 偽裝的私有 IP 上網，就像你家路由器幫所有裝置做 NAT 一樣。VM 可以主動連出去，但外面（包含 host 自己）連不進來，多台 VM 用 NAT 也彼此看不到對方。適合「我只是想讓這台 VM 能上網裝套件」的單純需求。

**2. NAT Network**  
NAT 的進化版，多了一個關鍵能力：同一個 NAT Network 底下的多台 VM 可以互相看到、互相連線，同時還能上網。差異就在「VM↔VM」這格從 ❌ 變成 ✅。

**3. Bridged（橋接）**  
VM 的虛擬網卡直接「橋接」到你的實體網卡，VM 會像一台獨立的實體機器一樣，從你家路由器拿到一個跟你筆電同網段的真實 IP。三邊（外網、host、VM 間）全部互通。但這也代表你的 Kali VM 現在跟你家其他裝置在同一個網段上，是可以被發現、被掃描到的。

**4. Host-only**  
建立一個只存在於 host 和 VM 之間的私有虛擬網段（例如 `vboxnet0`，網段像 `192.168.56.0/24`）。VM 之間互通、host 也能連進 VM，但這整組網段完全連不到外網。這是這週要設定的模式。

**5. Internal Network**  
比 Host-only 更封閉——VM 之間可以互通，但連 host 自己都連不進去。是五種裡面隔離程度最高的，適合你完全不希望任何外部（連你自己的 host）介入的純攻防演練場景，但管理上比較麻煩（沒辦法直接從 host SSH 進去）。


## VirtualBox 虛擬網路模式對照表

| 模式 | VM↔外網 | VM↔Host | VM↔VM | 典型用途 |
|------|:-------:|:-------:|:-----:|----------|
| NAT | ✅ | ❌ | ❌ | 單一 VM 上網 |
| NAT Network | ✅ | ❌ | ✅ | 多 VM 上網又互通 |
| Bridged | ✅ | ✅ | ✅ | VM 拿實體網段 IP，當 LAN 上獨立機器 |
| Host-only | ❌ | ✅ | ✅ | 隔離實驗網段（Phase 2 攻防用） |
| Internal | ❌ | ❌ | ✅ | 最隔離的攻防網段 |

> 隔離程度：Internal > Host-only > NAT > NAT Network > Bridged


