import random 

print('Jogo da Adivinhação!')
print('O computador pensou em um número entre 1 a 100, tente acertar!')

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    try:
        chute_str = input('Chute um número: ')
        chute = int(chute_str)
    except ValueError:
        print('Ei! Digite apenas números inteiros.')
        continue 

    tentativas = tentativas + 1

    if chute == numero_secreto:
        print(f'Parabéns! Você acertou o número {numero_secreto}!')
        print(f'Você precisou de {tentativas} tentativas.')
        break

    elif chute > numero_secreto:
        print(f'Chutou alto! O número secreto é MENOR que {chute}.')

    elif chute < numero_secreto:
        print(f'Chutou baixo! O número secreto é MAIOR que {chute}.')

print('Fim de Jogo.')

