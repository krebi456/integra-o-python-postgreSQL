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

cursor.execute(""" 
    SELECT
    produtos.id,
    produtos.nome,
    produtos.preco,
    usuarios.nome
    FROM produtos
    INNER JOIN usuarios
    ON produtos.usuario_id = usuarios.id
    """)
dados = cursor.fetchall()

for produto in dados:
    print(produto)

cursor.close()
conexao.close()