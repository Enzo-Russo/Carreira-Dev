import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='sistema_vendas'
)

cursor = conexao.cursor()
print('Sistema de busca de produtos! ou digite "sair" para fechar')
print('-' * 40)

while True:
    categoria_desejada = input('Busque a categoria que deseja: ').strip()

    if categoria_desejada.lower() == 'sair':
       print('Fechando sistema...')
       break

    try:    

       sql = 'SELECT * FROM produtos WHERE categoria = %s'
       cursor.execute(sql, (categoria_desejada,))
       produtos_encontrados = cursor.fetchall()
    
       if len(produtos_encontrados) == 0:
          print(f'Nenhuma categoria "{categoria_desejada}" encontrada. Tente outra.')
          continue
       
       print(f'\nEncontrei {len(produtos_encontrados)} produtos na categoria "{categoria_desejada}":')
       print('-' * 40)

       for produto in produtos_encontrados:
          print(f'Produto: {produto[1]} | Preço: R$ {produto[2]}')


    except Exception as erro:
       print(f'Ocorreu um erro no banco de dados: {erro}')

cursor.close()
conexao.close()


