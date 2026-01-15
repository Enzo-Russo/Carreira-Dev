# Sistema de vendas
def limpar_preco(valor_sujo):
   passo1 = valor_sujo.strip()
   passo2 = passo1.replace('R$', '')
   passo3 = passo2.replace('.', '')
   passo4 = passo3.replace(',', '.')
   numero_final = float(passo4)
   return numero_final

vendas = []

while True:
    nome_input = input('Nome do produto (ou "sair"): ')

    if nome_input.lower() == 'sair':
        break

    preco_texto = input('Preço do produto (pode usar R$ e vírgula): ')

    preco_limpo = limpar_preco(preco_texto)

    nova_venda = {
        'produto': nome_input,
        'valor': preco_limpo
    }

    vendas.append(nova_venda)
    print(f'Cadastrado: {nova_venda}')

print('-' * 40)
print('Relatório:')

for item in vendas:
    print(f'Produto: {item["produto"]} | Preço: R$ {item["valor"]:.2f}')
