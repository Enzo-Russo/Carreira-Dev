# Exercício Iterando strings com while
# Coloque um * em cada letra = *E*n*z*o* *R*u*s*s*o*

nome = 'Enzo Russo'
indice = 0
novo_nome = ''

while indice < len(nome): # enquanto indice for menor do que len(quantidade) da variável nome
    letra = nome[indice] # cria a variável letra = 'Enzo Russo', 0 
# [indice] -> busca o indice na variável nome, no caso, indice é 0, 
# então ele busca o indice 0 na varíavel nome que é 'Enzo Russo'.
    novo_nome += f'*{letra}' # cria a variável novo_nome = '' (da variável criada anteriormente), 
# E (porque o indice é 0, que é o indice da letra 'E' no nome 'Enzo Russo'.)
# Use o f' para adicionar o * na variável novo nome
    indice += 1 # soma 1 no indice e volta para o while 

print(novo_nome)