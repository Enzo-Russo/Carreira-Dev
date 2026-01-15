
produtos = ['Iphone', 'Ipad', 'Airpods', 'Macbook']

while True:
      
    print(f'\nEstoque atual: {produtos}')
    
    produto_str = input('Digite um produto que deseja remover (Ou Sair para encerrar):  ')

    if produto_str.lower() == 'sair':
       break
    
    if produto_str not in produtos:
        print(f'Este produto "{produto_str}" digitado não foi encontrado')
        continue

    print(f'Produto "{produto_str}" encontrado no estoque')

    produtos.remove(produto_str)
    print(f'Produto "{produto_str}" removido com sucesso!')

    
        