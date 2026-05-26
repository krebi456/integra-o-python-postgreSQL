import psycopg2
import os
from dotenv import load_dotenv
from time import sleep
import bcrypt

load_dotenv()

conexao = psycopg2.connect(
	host = "localhost",
	database = "projeto_banco_de_dados",
	user = "postgres",
	password = os.getenv("DB_PASSWORD"),
	port = "5432"
	)
user_nome = str(input("insira seu nome: "))

sleep(1)

user_idade = int(input("insira sua idade: "))

sleep(1)

user_email = str(input("insira seu email: "))

sleep(1)

user_senha = str(input("insira sua senha: "))

hash_senha = bcrypt.hashpw(
    user_senha.encode("utf-8"),
    bcrypt.gensalt()
)


for c in range(3,0,-1):
    print(c)
    sleep(1)

print("conectado com sucesso!")

sleep(1)

cursor = conexao.cursor()


cursor.execute(
    f"INSERT INTO usuarios (nome,idade,email,senha) VALUES (%s,%s,%s,%s);",
    (user_nome,user_idade,user_email,hash_senha.decode("utf-8"))
)

conexao.commit()

print("Tabela atualizada!")

cursor.close()
conexao.close()