from flask import Flask, Response
from flask_cors import CORS
import time
import json

app = Flask(__name__)
CORS(app)  # 允许跨域请求

@app.route('/stream')
def stream():
    def generate():
        for i in range(10):
            data = {
                "message": f"Hello, this is message {i}",
                "timestamp": time.time()
            }
            yield f"data: {json.dumps(data)}\n\n"
            time.sleep(1)  # 模拟每秒发送一条消息
    return Response(generate(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)