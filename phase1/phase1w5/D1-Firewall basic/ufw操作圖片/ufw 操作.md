# 啟用 ufw
sudo ufw enable
sudo ufw status verbose

# 預設策略：進來全擋、出去全放
sudo ufw default deny incoming
sudo ufw default allow outgoing

# 開放特定 port
sudo ufw allow 22/tcp        # SSH
sudo ufw allow 80/tcp        # HTTP
sudo ufw allow 443/tcp       # HTTPS

# 限制來源 IP（這個概念之後在 GCP Firewall Rules 會再用到）
sudo ufw allow from 192.168.1.0/24 to any port 22

# 刪除規則
sudo ufw delete allow 80/tcp

# 查看規則編號（方便刪除）
sudo ufw status numbered

|ufw|GCP Firewall Rules|
|---|---|
|`allow from IP to port`|source ranges + allowed ports|
|`default deny incoming`|implicit deny（GCP 預設行為）|
|規則有優先順序|priority 數字越小越優先|