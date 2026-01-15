
def limpar_preco(valor_sujo):
   passo1 = valor_sujo.strip()
   passo2 = passo1.replace('R$', '')
   passo3 = passo2.replace(',', '.')
   numero_final = float(passo3)
   return numero_final

preco_bagunçado = ' R$ 1200,50 '
resultado = limpar_preco(preco_bagunçado)

print(f'Entrou: "{preco_bagunçado}')
print(f'Saiu: {resultado}')
