import random

print('JOKENPO')
print('1 - PEDRA | 2 - PAPEL | 3 - TESOURA')

pedra = 1
papel = 2
tesoura = 3

while True:
    pc = random.randint(1, 3)
    try:
        usuario_str = input('Escolha um número de 1 a 3! Ou 0 para sair: ')
        usuario = int(usuario_str)

    except ValueError:
        print('Ei, digite apenas números!')
        continue
    
    if usuario == 0:
        print('Saindo...')
        break
    
    if usuario not in [1, 2, 3]:
        print('Número inválido! Escolha 1, 2 ou 3.')
        continue
    
    print(f'O Computador escolheu: {pc}')
    print('---')

    if usuario == pc:
        print('Empate!')
    elif usuario == 1 and pc == 3:
        print('Usuário é o Vencedor!')
    elif usuario == 2 and pc == 1:
        print('Usuário é o Vencedor!')
    elif usuario == 3 and pc == 2:
        print('Usuário é o Vencedor!')
    else:
        print('PC é o Vencedor!')

    

    



    
    


