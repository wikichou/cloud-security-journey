基本上，可以想像成我開了一個name space，他會有著下面表格中六種不同類型的table，這些table會代表這個name space可以看到的，或是說可以應用的相關的資源，然後process是屬於一個特定的name space

| namespace | 隔離什麼                              |
| --------- | --------------------------------- |
| PID       | process ID 空間                     |
| NET       | 網路 stack（interface、routing table） |
| MNT       | 掛載點（檔案系統視角）                       |
| UTS       | hostname                          |
| IPC       | 行程間通訊                             |
| USER      | UID/GID 映射                        |
![[PID.png]]
這是 `/proc/self/ns` 的內容，顯示當前 process 所屬的各個 namespace symlink。圖中每個 symlink 後面的數字（如 `[4026531836]`）是 inode number，唯一識別一個 namespace 實例——兩個 process 如果同一個 namespace 類型的 inode 號相同，代表它們共用同一個 namespace，這是判斷隔離是否生效的實用方式。

```
sudo unshare --pid --fork --mount-proc bash
```

|部分|作用|
|---|---|
|`unshare`|系統呼叫 `unshare()` 的 CLI 包裝，功能是「建立新的 namespace 並在裡面跑一個程式」|
|`--pid`|指定要新建的是 **PID namespace**——新程式會有自己獨立的 PID 編號空間|
|`--fork`|先 `fork()` 出一個子行程，再讓子行程進入新的 PID namespace 執行 `bash`|
|`--mount-proc`|在新 namespace 裡重新 mount 一份 `/proc`，讓 `ps` 之類的工具能正確反映新的 PID 空間|
|`bash`|進入新 namespace 後要執行的程式|

我們可以利用這樣的指令建立一個新的namespace
![[name space practice.png]]
這樣去看就會發現它內部的process跟剛剛前面看到的完全不一樣。bash 成為 PID 1 代表它在這個隔離空間裡扮演 init 的角色，這也是 Docker container 內部的運作原理基礎。