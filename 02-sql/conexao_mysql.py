import pymysql

# 1. Configurando a conexão (A "Ligação" para o servidor)
conexao = pymysql.connect(
    host='localhost',        # O banco está no seu próprio PC
    user='root',             # Usuário padrão
    password='1234', # <--- TROQUE PELA SUA SENHA!
    database='sistema_vendas' # O banco que criamos no Workbench
)

print("Conexão realizada com sucesso!")

# 2. Criando o Cursor (O "Mouse" que seleciona as coisas lá dentro)
cursor = conexao.cursor()

# 3. Executando um comando SQL pelo Python
print("Consultando produtos...")
cursor.execute("SELECT * FROM produtos")

# 4. Pegando e exibindo os resultados
produtos = cursor.fetchall() # Pega TUDO o que a consulta achou

for produto in produtos:
    # O banco devolve uma Tupla: (id, nome, preco, estoque)
    print(f"Produto: {produto[1]} | Preço: R$ {produto[2]} | Estoque: {produto[3]}")

# 5. Fechando a porta (Sempre feche a conexão!)
cursor.close()
conexao.close()