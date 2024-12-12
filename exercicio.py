#1. Você está analisando um conjunto de dados de vendas e 
# precisa garantir que todos os registros tenham valores positivos 
# para quantidade e preço. Escreva um programa que verifique esses 
# campos e imprima "Dados válidos" se ambos forem positivos ou 
# "Dados inválidos" caso contrário.

# quantidade_usuario = int(input("Digite a quantidade: "))
# preco_usuario = int(input("Digite o preço: "))

# if quantidade_usuario > 0 and preco_usuario > 0:
#     print("Dados válidos")
# else:
#     print("Dados inválidos")

# Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de 
# sensores IoT. Os dados incluem medições de temperatura. 
# Você precisa classificar cada leitura como 'Baixa', 
# 'Normal' ou 'Alta'. Considerando que:

# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

# temp = float(input("Digite a temperatura para medição: "))

# if temp < 18:
#     print(f"{temp}°C é uma temperatura baixa")
# elif temp >= 18 and temp <= 26:
#     print(f"{temp}°C é uma temperatura normal")
# else:
#     print(f"{temp}°C é uma temperatura alta")