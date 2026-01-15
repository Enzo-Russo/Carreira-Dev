import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='sistema_vendas'
)

cursor = conexao.cursor()

print('Sistema de Atualização de Produtos') 

nome_produto = input('Qual o nome do produto que deseja atualizar?: ')
nova_categoria = input(f'Qual a categoria para {nome_produto}?: ')

try:
    sql = 'UPDATE produtos SET categoria = %s WHERE nome = %s'
    cursor.execute(sql,(nova_categoria, nome_produto,))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f'Sucesso! O produto {nome_produto} agora é da categoria {nova_categoria}.')
    else:
        print(f'Não encontreu nenhum produto chamado {nome_produto} para atualizar')    

except Exception as erro: 
    print(f'Erro: {erro}')

finally:
    cursor.close()
    conexao.close()      
    



