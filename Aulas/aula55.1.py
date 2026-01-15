"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Exercício 2

horario = input('Que horas são?: ')

try:
    horario = float(horario)

    if horario >= 0 and horario <= 11:
        print('Bom dia!')

    elif horario >= 12 and horario <= 17:
       print('Boa tarde')

    elif horario >= 18 and horario <= 23:
       print('Boa noite')

    else:
       print('Digite um horário válido')

except:
    print('Digite novamente...')
