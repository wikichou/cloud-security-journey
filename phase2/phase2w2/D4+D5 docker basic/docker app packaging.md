
今天練習自己打包一個image，打包一個基本的python如下

建立app.py
```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from my first container!\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

建立requirements.txt
```
flask
```

建立Dockerfile(沒有副檔名)
```
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

然後跑

```
docker build -t myflask .
```
成功之後應該可以看到剛剛包的myflask，看到有成功就可以用run把他跑起來看看

![[docker my image.png]]![[myflask.png]]

現在server已經起來了，就可以curl跑看看

![[curl localhost.png]]

明顯可以看出來是成功的

接著把app.py稍微改動一下重新build一次
![[rebuild.png]]

可以看出來copy . .以上的都直接用上cache了，這裡講一個重點

Docker 的 layer 快取是**鏈式**的,規則很簡單:

> **某一層失效,它後面的所有層全部跟著失效。**

所以說前面的因為已經有build過不用再一次，但是這一層因為app有改過所以要重新build一次，也就是說如果要加速的話要非常注重layer的順序，改動頻率低的要放在前面，就不會一直被重新build


接著去看容器裡的process
![[proc1.png]]
可以看到PID 1就是python app.py而不是shell，也就是代表docker container本身就是一整個process，負責跑你的app，如果container生命週期結束了，那PID1自然就會消失