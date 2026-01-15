#Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
#menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
#"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

# Exercício 3:

nome_usuario = input('Digite seu nome por favor: ')

tamanho_nome = len(nome_usuario)

if tamanho_nome <= 4:
    print('Seu nome é curto')

elif tamanho_nome <= 5 and tamanho_nome <= 6:
    print('Seu nome é normal')

else:
    print('Seu nome é muito grande')