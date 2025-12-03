from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/orders")
def orders():
    return jsonify([
        {"id": 1, "user_id": 1, "produto": "Camiseta"},
        {"id": 2, "user_id": 1, "produto": "Livro"},
        {"id": 3, "user_id": 2, "produto": "Mouse"}
    ])

@app.route("/")
def home():
    return {"message": "Serviço de Pedidos ativo"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6002)
