import psycopg2
from time import sleep
conexao = psycopg2.connect(
	host = "localhost",
	database = "projeto_banco_de_dados",
	user = "postgres",
	password = "123456",
	port = "5432"
	)
user_nome = str(input("insira seu nome: "))
sleep(1)
user_idade = int(input("insira sua idade: "))
for c in range(3,0,-1):
    print(c)
    sleep(1)

print("conectado com sucesso!")

sleep(1)

cursor = conexao.cursor()


cursor.execute(f"""INSERT INTO usuarios (nome,idade) VALUES ({user_nome}, {user_idade})""")

conexao.commit()

print("Tabela atualizada!")

cursor.close()
conexao.close()