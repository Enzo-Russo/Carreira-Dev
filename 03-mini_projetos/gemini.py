# main.py - Dia 1: Leitura Básica

# 1. Vamos definir o nome do arquivo numa variável (Aula de Variáveis)
nome_arquivo = 'vendas.csv'

print(f"--- Lendo o arquivo: {nome_arquivo} ---")

# 2. Abrir o arquivo (Comando padrão do Python)
arquivo = open(nome_arquivo, 'r', encoding='utf-8')

# 3. Ler o conteúdo
conteudo = arquivo.read()

# 4. Mostrar na tela (Aula de Print)
print(conteudo)

# 5. Fechar o arquivo (Boa prática)
arquivo.close()

print("--- Fim da leitura ---")