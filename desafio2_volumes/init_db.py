import sqlite3

conn = sqlite3.connect("/data/banco.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        curso TEXT
    );
""")

cursor.execute("INSERT INTO alunos (nome, curso) VALUES ('Myllena', 'Computação')")
cursor.execute("INSERT INTO alunos (nome, curso) VALUES ('João', 'Engenharia')")
cursor.execute("INSERT INTO alunos (nome, curso) VALUES ('Maria', 'ADS')")

conn.commit()
conn.close()

print("Banco criado e dados inseridos com sucesso!")
