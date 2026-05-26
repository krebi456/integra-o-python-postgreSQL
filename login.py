import psycopg2
import os
from dotenv import load_dotenv
import bcrypt

load_dotenv()

conexao = psycopg2.connect(
    host = "localhost",
	    database = "projeto_banco_de_dados",
	    user = "postgres",
	    password = os.getenv("DB_PASSWORD"),
	    port = "5432"
)

cursor = conexao.cursor()

email = input("Email: ")
senha = input("Senha: ")

cursor.execute("""
SELECT senha
FROM usuarios
WHERE email = %s
""", (email,))

resultado = cursor.fetchone()

if resultado is None:
    print("Usuário não encontrado!")

else:
    senha_hash = resultado[0]

    if bcrypt.checkpw(
        senha.encode('utf-8'),
        senha_hash.encode('utf-8')
    ):
        print("Login realizado!")
    else:
        print("Senha incorreta!")

cursor.close()
conexao.close()