from flask import Flask, Response, send_from_directory
from flask_cors import CORS
import time
import json
import requests

app = Flask(__name__)
CORS(app)  # 允许跨域请求

@app.route('/stream')
def stream():
    def generate():
        for i in range(5):
            data = {
                "message": f"Hello, this is message {i}",
                "timestamp": time.time()
            }
            yield f"data: {json.dumps(data)}\n\n"
            time.sleep(1)
        # 发送结束事件
        yield "event: end\ndata: {}\n\n"
    return Response(generate(), content_type='text/event-stream')


@app.route('/stream2')
def stream2():
    def generate():
        url = "https://llm.bjzntd.com/api/v2/chat"
        headers = {
            "Content-Type": "application/json",
            # 如果需要认证，添加认证头
        }
        payload = {
            "messages": [
                {"role": "user", "content": "怎么种苹果？"}
            ],
            "stream": True
        }
        
        with requests.post(url, json=payload, headers=headers, stream=True) as response:
            for chunk in response.iter_content(chunk_size=None):
                if chunk:
                    yield f"{chunk.decode('utf-8')}\n\n"
            # 发送结束事件
            yield "event: end\ndata: {}\n\n"

    return Response(generate(), content_type='text/event-stream')


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/index.html')
def index_html():
    return send_from_directory('.', 'index.html')

@app.route('/index2.html')
def index2_html():
    return send_from_directory('.', 'index2.html')

if __name__ == '__main__':
    app.run(debug=True)