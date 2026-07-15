from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def hello():
    count = r.incr('hits')
    return f'Hello! 這個頁面被訪問了 {count} 次\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)