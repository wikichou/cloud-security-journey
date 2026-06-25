### routing table
有問題先找他，如果routing時裡面找不到目的地就會收到ICMP unreachable，也可以設定一個default IP，也就是last resort，流量不知道要去哪時就去他那邊

### DHCP
注意DHCP 的IP pool不要用完，如果用完了新的裝置只會拿到APIPA ，這只能讓你在local用但不能做routing，同時也要注意手動設定IP的裝置有沒有跟DHCP分配出去的重複，或是有兩個DHCP server在做分發