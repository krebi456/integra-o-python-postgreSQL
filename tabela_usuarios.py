import psycopg2
import os
from dotenv import load_dotenv

load_dotenv

conexao = psycopg2.connect(
	host = "localhost",
	database = "projeto_banco_de_dados",
	user = "postgres",
	password = os.getenv("DB_PASSWORD"),
	port = "5432"
	)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuarios")

dados = cursor.fetchall()

for usuario in dados:
    print(usuario)

cursor.close()
conexao.close()