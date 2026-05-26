import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conexao = psycopg2.connect(
	host = "localhost",
	database = "projeto_banco_de_dados",
	user = "postgres",
	password = os.getenv("DB_PASSWORD"),
	port = "5432"
	)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM produtos;")

dados = cursor.fetchall()

for produto in dados:
    print(produto)

cursor.close()
conexao.close()