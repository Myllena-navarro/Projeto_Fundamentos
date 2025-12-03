from flask import Flask, jsonify
import requests

app = Flask(__name__)

MICROSERVICO_A_URL = "http://servico_a:5001/users"

@app.route("/")
def home():
    return {"message": "Microsserviço B - Consumidor"}

@app.route("/usuarios-detalhados")
def detalhados():
    try:
        resposta = requests.get(MICROSERVICO_A_URL)
        usuarios = resposta.json()

        lista = []
        for u in usuarios:
            status = "ativo" if u["ativo"] else "inativo"
            lista.append({
                "id": u["id"],
                "nome": u["nome"],
                "status_desc": f"Usuário {u['nome']} está {status} no sistema."
            })

        return jsonify(lista)

    except Exception as e:
        return {"erro": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
