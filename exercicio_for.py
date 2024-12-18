####exercicios for
# 
# 
# ### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada
#  palavra única aparece nele.


# import string

# texto_usuario=input("Digite uma frase por favor: ")

# texto_usuario = texto_usuario.lower() 
# for pontuacao in string.punctuation:
#     texto_usuario= texto_usuario.replace(pontuacao, "")


# divisao_de_palavras= texto_usuario.split(" ")# dividindo o texto em palavras
# contagem_de_palavras = {} # iniciando o dicionario vazio para armazenar a contagem

# for palavra_atual in divisao_de_palavras:

#     if palavra_atual in contagem_de_palavras:
#         contagem_de_palavras [palavra_atual] += 1
#     else:
#         contagem_de_palavras[palavra_atual] = 1


# print("Contagem de palavras no texto: \n ")
# for palavra_atual, quantidade in contagem_de_palavras.items():
#     print(f"{palavra_atual} : {quantidade}")









### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros= [10,20,30,40,50]
minimo = min(numeros)
maximo = max(numeros)
normalizados = []

for valor_atual in numeros:
    valor_normalizado =(valor_atual - minimo) / (maximo - minimo)
    normalizados.append(valor_normalizado)

print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.