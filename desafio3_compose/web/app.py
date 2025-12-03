from flask import Flask, jsonify
import psycopg2
import redis

app = Flask(__name__)

# Conectar ao Redis
cache = redis.Redis(host="cache", port=6379)

@app.route("/")
def home():
    return {"message": "Aplicação Web no ar (serviço web)!"}

@app.route("/cache")
def cache_test():
    cache.incr("visitas")
    return {"visitas": int(cache.get("visitas"))}

@app.route("/db")
def db_test():
    try:
        conn = psycopg2.connect(
            dbname="meubanco",
            user="postgres",
            password="postgres",
            host="db",
            port=5432
        )
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        versao = cursor.fetchone()
        cursor.close()
        conn.close()
        return {"postgres_version": versao}
    except Exception as e:
        return {"erro": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
