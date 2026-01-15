import pymysql
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='sistema_vendas'
)

cursor = conexao.cursor() 

print('Sistema de remover produtos das categorias! Ou "sair" para fechar')

categoria_alvo = input('Qual categoria você quer APAGAR inteira? ')

try:
    sql = 'DELETE FROM produtos WHERE categoria = %s'
    cursor.execute(sql, (categoria_alvo,))
    conexao.commit()
    linhas_afetadas = cursor.rowcount
    
    if cursor.rowcount > 0:
       print(f'Sucesso! O produto {linhas_afetadas} produtos da categoria "{categoria_alvo} foram deletados"')

    else:
       print(f'Nenhum produto encontrado na categoria "{categoria_alvo}". Nada foi apagado')

except Exception as erro:
    print(f'Erro: {erro}')


finally:
    cursor.close()
    conexao.close()


