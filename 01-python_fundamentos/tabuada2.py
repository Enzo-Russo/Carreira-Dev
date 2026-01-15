print('VAMOS APRENDER TABUADA!')

numero_inteiro = 0

# FASE 1: Coleta e Validação (O padrão que você aprendeu)
while True:
    numero_str = input('Quer saber a tabuada de qual número? ')
    
    try:
        numero_inteiro = int(numero_str)
        print(f'Perfeito! Calculando a tabuada do {numero_inteiro}...\n')
        break # Sai do while e vai para o for
    except ValueError:
        print('Ei, isso não é um número inteiro. Tente de novo!')

# FASE 2: Processamento (O conteúdo novo do dia)
for i in range(1, 11):
    resultado = numero_inteiro * i
    print(f'{numero_inteiro} x {i} = {resultado}')