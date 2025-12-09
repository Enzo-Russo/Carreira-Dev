# Sistema de vendas

vendas = []

while True:
    nome_input = input('Nome do produto (ou "sair"): ')

    if nome_input.lower() == 'sair':
        break

    preco_input = float(input('Preço do produto: '))

    nova_venda = {
        'produto': nome_input,
        'valor': preco_input
    }

    vendas.append(nova_venda)
    print('Cadastrado!')

print('-' * 40)
print('Relatório:')

for item in vendas:
    print(f'Produto: {item["produto"]} | Preço: R$ {item["valor"]:.2f}')
