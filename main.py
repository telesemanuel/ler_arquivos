# Abrindo e lendo o arquivo
with open('example-countries-pt.csv', 'r', encoding='utf-8') as f:
    conteudo = f.read()

# Exibindo o conteúdo
print(conteudo)
