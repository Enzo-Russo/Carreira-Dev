#operadores in e not in

nome = 'Enzo'

nome = input('Digite seu nome' )
encontrar = input('Digite o que deseja encontrar' )

if encontrar in nome:
    print(f'{encontrar} está em' f'{nome}')
else:
    print(f'{encontrar} não está em' f'{nome}')