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
        print(f'Cliente: {nome} | Comprou: R$ {valor}')

print('Leitura finalizada')