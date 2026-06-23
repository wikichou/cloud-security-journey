## 檔案操作

| 功能      | Linux                  | CMD             | PowerShell                     |
| ------- | ---------------------- | --------------- | ------------------------------ |
| 列出檔案    | `ls -la`               | `dir`           | `Get-ChildItem`                |
| 建立目錄    | `mkdir`                | `mkdir`         | `New-Item -ItemType Directory` |
| 複製      | `cp`                   | `copy`          | `Copy-Item`                    |
| 移動/重新命名 | `mv`                   | `move` / `ren`  | `Move-Item`                    |
| 刪除      | `rm` / `rm -rf`        | `del` / `rmdir` | `Remove-Item`                  |
| 查看檔案內容  | `cat`                  | `type`          | `Get-Content`                  |
| 權限變更    | `chmod 755`            | —               | —                              |
| 擁有者變更   | `chown user:group`     | —               | —                              |
| 搜尋檔案    | `find / -name "*.log"` | `dir /s *.log`  | `Get-ChildItem -Recurse`       |
| 文字搜尋    | `grep -r "keyword"`    | `findstr`       | `Select-String`                |