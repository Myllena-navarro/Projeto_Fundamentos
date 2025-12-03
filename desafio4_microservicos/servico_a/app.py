from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def users():
    return jsonify([
        {"id": 1, "nome": "Myllena", "ativo": True},
        {"id": 2, "nome": "João", "ativo": True},
        {"id": 3, "nome": "Maria", "ativo": False}
    ])

@app.route("/")
def home():
    return {"message": "Microsserviço A - Usuários"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
