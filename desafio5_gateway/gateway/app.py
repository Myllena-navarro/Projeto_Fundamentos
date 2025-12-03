from flask import Flask, jsonify
import requests

app = Flask(__name__)

USERS_URL = "http://users_service:6001/users"
ORDERS_URL = "http://orders_service:6002/orders"

@app.route("/")
def home():
    return {"message": "API Gateway ativo"}

@app.route("/users")
def get_users():
    resposta = requests.get(USERS_URL)
    return jsonify(resposta.json())

@app.route("/orders")
def get_orders():
    resposta = requests.get(ORDERS_URL)
    return jsonify(resposta.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
