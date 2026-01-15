
total = 0

print('Iniciando processamento de vendas...')

with open('vendas.csv', 'r') as arquivo:
    for linha in arquivo:
        linha_limpa = linha.strip()

        if not linha_limpa:
            continue

        dados = linha_limpa.split(',')

        if len(dados) < 2:
            print(f'Linha ignorada (formato incorreto): {linha_limpa}')
            continue

        nome = dados[0]
        valor = dados[1]
        try:
            valor_float = float(valor.strip())
            total += valor_float
            print(f'Processando vendas de: {nome} | Valor: R$ {valor_float:.2f}')
        except ValueError:
            print(f'Erro ao converter valor para o cliente {nome}')

print('-' * 40)
print(f'Valor total de vendas: R$ {total:.2f}')