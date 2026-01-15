vendas = []

while True:
    produto_str = input('Digite um produto: (ou sair para encerrar): ')

    if produto_str.lower() == 'sair':
        break

    vendas.append(produto_str)
    print(f'Produto "{produto_str}" cadastrado com sucesso!')

print('-' * 30)
print('Relatório de Vendas:')

for venda in vendas:
    print(venda)

        





    
