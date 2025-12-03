from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def users():
    return jsonify([
        {"id": 1, "nome": "Myllena"},
        {"id": 2, "nome": "João"},
        {"id": 3, "nome": "Ana"}
    ])

@app.route("/")
def home():
    return {"message": "Serviço de Usuários ativo"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6001)
