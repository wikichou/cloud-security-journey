

```
ls -la /proc/1/ns/    # 對照週一!容器有自己一組 namespace(中括號的 inode 數字跟 host 不同)
ps aux                
```

![[docker ubuntu.png]]

這是從官方的repository拉的一個ubuntu image跑起來之後，去看他proc id為1的name space
此時我還沒有做任何操作，但可以看到所有的name space都已經被建立好了，我不需要手動config

![[ps aux.png]]

這裡也能看出來說他的PID是1，跟前幾天建立一個新的name space時的狀況一模一樣
