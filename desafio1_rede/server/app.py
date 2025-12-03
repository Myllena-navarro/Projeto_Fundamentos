from flask import Flask, request, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    host = socket.gethostname()
    return jsonify({
        "message": "Olá do servidor Flask!",
        "time": now,
        "host": host
    })

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify({
        "received": data,
        "note": "Este endpoint ilustra comunicação entre containers"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
