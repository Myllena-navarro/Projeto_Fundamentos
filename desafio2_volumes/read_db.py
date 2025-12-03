import sqlite3

conn = sqlite3.connect("/data/banco.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM alunos")
dados = cursor.fetchall()

print("Dados encontrados:")
for linha in dados:
    print(linha)

conn.close()
