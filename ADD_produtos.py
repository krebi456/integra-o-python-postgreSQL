import psycopg2
import os
from dotenv import load_dotenv
from time import sleep

#111

load_dotenv()

conexao = psycopg2.connect(
	    host = "localhost",
	    database = "projeto_banco_de_dados",
	    user = "postgres",
	    password = os.getenv("DB_PASSWORD"),
	    port = "5432"
	    )

nome = input("nome do produto: ")

sleep(1)

preco = float(input("preço do produto: "))

sleep(1)

usuario_id = int(input("id do usuario: "))

sleep(1)

cursor = conexao.cursor()

cursor.execute("INSERT INTO produtos(nome, preco, usuario_id) VALUES (%s,%s,%s)", (nome,preco,usuario_id))

conexao.commit()

print("produto cadastrado!")

cursor.close()
conexao.close()