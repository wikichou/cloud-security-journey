今天的目標是先把這周的nginx+flask+Redis的架構建起來
### IP

compose會自動幫每一個專案建立user-defined network，在這個network裡面service本身的名字就是DNS hostname。
假設說我今天有一個
```
services:
  redis:
    image: redis:alpine
  app:
    build: ./app
```
這樣的redis service，而我的flask想要連上他的話不用用IP，直接

```
r = redis.Redis(host='redis', port=6379)
```
這樣子就好，redis這個字串會被compose裡面的DNS解析成正確的container IP。

### depends_on
有時候我們會需要確保啟動某個container前要先啟動另一個container，那可以這樣寫
```
services:
  app:
    build: ./app
    depends_on:
      - redis
  redis:
    image: redis:alpine
```
這樣寫的意思就是先啟動redis，再啟動app，不過這要注意的是這只保證redis這個container會先被啟動，但是不代表redis這個service本身已經ready to connect了。

再來開始實際建立這個三層架構，可以參考three tier裡面的內容，簡單來說就是寫了一個app是用來計算他被訪問了幾次，然後利用compose來同時啟動nginx/flask/redis做成一個簡易的server服務