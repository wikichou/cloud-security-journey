**namespace 代表「這個 process 能『看到』什麼」;cgroup 代表「這一群 process 能『用掉』多少資源」。** 兩者是**完全獨立的兩套 kernel 機制**,剛好互補。

cgroup代表的是:OS的kernel層維護一個樹狀的結構，這個樹上的每一個node都代表一個cgroup(control group)，一組共用資源的限額的process群組，node內的process都會受到這個資源限額影響，重點是他是一棵樹，所以說 child cgroup 不能超過 parent 的上限（bounded by parent），但上限不會自動套用到 child，child 必須自己設定

root cgroup(整台機器所有資源)
├── system.slice(給系統 service 用)
│   ├── ssh.service
│   └── docker.service
└── user.slice(給登入使用者用)
    └── user-1000.slice(你這個 user)
        └── session-x.scope(你這個 shell session)

像這樣一台機器ssh.service就會跟docker.service共用system.slice的資源配額

cgroup有v1和v2，而現代大多都用v2了，差別如下

- **v1(舊)**:每種資源(CPU、記憶體、IO)各自有**一棵獨立的樹**,同一個 process 在不同資源樹上可能被放在不同節點 → 管理複雜、容易出錯
- **v2(新)**:**單一一棵統一的樹**,一個 process 就掛在樹上一個節點,所有資源類型統一由這個節點的位置決定 → 簡潔、一致

樹上的node我可以掛上不同的controller，他們負責管理不同的資源

| Controller | 管什麼            |
| ---------- | -------------- |
| memory     | 記憶體上限          |
| cpu        | CPU 配額         |
| pids       | 最多能開幾個 process |
| io         | 磁碟 I/O 速率上限   |

## cgroup 在 filesystem 的位置

cgroup v2 掛載在 `/sys/fs/cgroup/`，樹上每一個 node 就是這個目錄下的一個子資料夾，資源限制就是資料夾內的檔案，直接讀寫這些檔案就能查看或調整限額。

```bash
ls /sys/fs/cgroup/                               # 看整棵樹的根
cat /sys/fs/cgroup/user.slice/user-1000.slice/memory.max   # 查某個 cgroup 的記憶體上限
```

### 核心檔案

| 檔案                     | 用途                                  |
| ---------------------- | ----------------------------------- |
| `cgroup.procs`         | 列出這個 cgroup 內的 PID；寫入 PID 可把 process 移進來 |
| `memory.max`           | 記憶體上限（`max` 表示不限制）                  |
| `cpu.max`              | CPU 配額，格式為 `quota period`           |
| `cgroup.subtree_control` | 控制哪些 controller 要傳遞給 child cgroup  |

把 process 加入某個 cgroup：

```bash
echo $$ > /sys/fs/cgroup/mygroup/cgroup.procs
```

### subtree_control

v2 的規則：要讓 child cgroup 能使用某個 controller，parent 必須先在 `cgroup.subtree_control` 啟用它，否則 child 寫入 `memory.max` 等檔案會沒有效果。

```bash
echo "+memory +cpu" > /sys/fs/cgroup/mygroup/cgroup.subtree_control
```

## Docker 如何使用 cgroup

Docker 每啟動一個容器，就會在 cgroup 樹上建立一個對應的 scope，`docker run` 的 `--memory`、`--cpus` 等參數本質上就是在寫這個目錄下的檔案。

```bash
# 查看某個容器的 cgroup
ls /sys/fs/cgroup/system.slice/docker-<container-id>.scope/

# 查看容器的記憶體上限
cat /sys/fs/cgroup/system.slice/docker-<container-id>.scope/memory.max
```

這也是為什麼容器逃逸（container escape）後，攻擊者會去讀這些檔案來判斷目前在哪個 cgroup、有沒有資源限制被鬆綁。

```
cat /proc/$$/cgroup
```


![[cgroup.png]]
從這張圖中可以看出來目前的shell是掛在user.slice之下的

```
systemd-cgls
```
![[cgroup tree.png]]

這張圖則是畫出了整顆cgroup tree

```
systemd-cgtop
```

![[cgtop.png]]
這裡則是可以看到動態的資源使用狀況