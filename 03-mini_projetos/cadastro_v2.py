import pymysql

# 1. Configurar Conexão
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='1234', # <--- SUA SENHA AQUI
    database='sistema_vendas'
)

print("Sistema de Cadastro de Produtos")
print("-" * 30)

# 2. Coletar dados do usuário
nome = input("Digite o nome do produto: ")

# Tratamento simples para garantir que preço e estoque sejam números
try:
    preco = float(input("Digite o preço (ex: 1200.50): "))
    estoque = int(input("Digite a quantidade em estoque: "))
    categoria = str(input('Digite a categoria do produto: '))
except ValueError:
    print("Erro: Preço ou estoque inválidos. Use pontos para centavos.")
    exit() # Encerra o programa se deu erro

try:
    cursor = conexao.cursor()

    # 3. O Comando SQL (Note o %s - Isso é a segurança!)
    sql = "INSERT INTO produtos (nome, preco, estoque, categoria) VALUES (%s, %s, %s, %s)"
    
    # 4. Executar (Passamos os valores numa Tupla separada)
    # O PyMySQL substitui os %s pelos valores na ordem certa
    cursor.execute(sql, (nome, preco, estoque, categoria))

    # 5. O PULO DO GATO: COMMIT
    # Sem isso, o banco ignora a inserção!
    conexao.commit() 
    
    print(f"\n✅ Sucesso! Produto '{nome}' cadastrado no banco com a categoria {categoria}!")

except Exception as erro:
    print(f"❌ Ocorreu um erro no banco de dados: {erro}")

finally:
    # 6. Fechar tudo
    cursor.close()
    conexao.close()