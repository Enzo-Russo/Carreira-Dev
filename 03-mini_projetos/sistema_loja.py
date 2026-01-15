import pymysql

# 1. Conexão Global (Fica fora das funções para todos usarem)
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='1234', # <--- CONFIRA A SENHA
    database='sistema_vendas'
)
conexao.autocommit(True) # O pulo do gato: Commit automático para tudo!
cursor = conexao.cursor()

# --- ÁREA DAS FUNÇÕES (AS GAVETAS) ---

def cadastrar_produto():
    print("\n--- CADASTRAR NOVO PRODUTO ---")
    
    # Coletando dados
    nome = input("Nome do produto: ")
    try:
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
        categoria = input("Categoria: ")
        
        sql = "INSERT INTO produtos (nome, preco, estoque, categoria) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome, preco, estoque, categoria))
        
        # Como ativamos o autocommit lá em cima, não precisa de conexao.commit() aqui!
        print(f"✅ Sucesso! '{nome}' cadastrado.")
        
    except ValueError:
        print("❌ Erro: Preço ou Estoque devem ser números. Tente novamente.")
    except Exception as erro:
        print(f"❌ Erro no banco: {erro}")

    
    

def listar_produtos():
    print("\n--- LISTA DE PRODUTOS ---")
    sql = 'SELECT * FROM produtos'
    cursor.execute(sql)
    produtos = cursor.fetchall()

    if len(produtos) == 0:
        print('Nenhum produto encontrado.')
    else:
        print(f'{"ID":<5} | {"NOME":<20} | {"PREÇO":<10} | {"ESTOQUE":<8} | {"CATEGORIA":}')
        for p in produtos:
            print(f'{p[0]:<5} | {p[1]:<20} | R$ {p[2]:<7} | {p[3]:<8} | {p[4]}')
    
    input('Aperte ENTER para seguir')

def atualizar_produto():
    print("\n--- ATUALIZAR PRODUTO ---")
    listar_produtos() # Mostra a lista antes para você escolher o ID. Esperto, né?
    
    try:
        id_produto = int(input("\nDigite o ID do produto que quer atualizar: "))
        
        # O que vamos mudar?
        novo_preco = float(input("Novo Preço: "))
        nova_categoria = input("Nova Categoria: ")

        sql = "UPDATE produtos SET preco = %s, categoria = %s WHERE id = %s"
        cursor.execute(sql, (novo_preco, nova_categoria, id_produto))

        if cursor.rowcount > 0:
            print(f"✅ Sucesso! Produto ID {id_produto} atualizado.")
        else:
            print("⚠️  ID não encontrado.")

    except ValueError:
        print("❌ Erro: Digite números válidos para ID e Preço.")
    except Exception as erro:
        print(f"❌ Erro no banco: {erro}")
        
    input("\nDigite ENTER para voltar ao menu...")
    

def deletar_produto():
    print("\n--- DELETAR PRODUTO ---")
    listar_produtos() # Mostra a lista para você não apagar o errado!
    
    try:
        id_produto = int(input("\nDigite o ID do produto que quer DELETAR: "))
        confirmacao = input(f"Tem certeza que quer apagar o ID {id_produto}? (S/N): ")

        if confirmacao.lower() == 's':
            sql = "DELETE FROM produtos WHERE id = %s"
            cursor.execute(sql, (id_produto,))

            if cursor.rowcount > 0:
                print(f"✅ Produto ID {id_produto} deletado com sucesso!")
            else:
                print("⚠️  ID não encontrado.")
        else:
            print("Operação cancelada.")

    except ValueError:
        print("❌ Erro: O ID deve ser um número.")
    except Exception as erro:
        print(f"❌ Erro no banco: {erro}")
        
    input("\nDigite ENTER para voltar ao menu...")

while True:
    print("\n" + "="*30)
    print("   SISTEMA DE GERENCIAMENTO")
    print("="*30)
    print("1. Cadastrar Novo Produto")
    print("2. Ver Produtos (Listar)")
    print("3. Atualizar Produto")
    print("4. Deletar Produto")
    print("5. Sair")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        cadastrar_produto() # Chama a gaveta de cadastro
    elif opcao == '2':
        listar_produtos()   # Chama a gaveta de lista
    elif opcao == '3':
        atualizar_produto() # Chama a gaveta de atualização
    elif opcao == '4':
        deletar_produto()   # Chama a gaveta de deletar
    elif opcao == '5':
        print("Saindo do sistema...")
        break # Quebra o loop e encerra
    else:
        print("❌ Opção inválida! Tente 1, 2, 3, 4 ou 5.")

   

# Fechar conexões ao sair do While
cursor.close()
conexao.close()
print("Sistema encerrado.")