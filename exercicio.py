#1. Você está analisando um conjunto de dados de vendas e 
# precisa garantir que todos os registros tenham valores positivos 
# para quantidade e preço. Escreva um programa que verifique esses 
# campos e imprima "Dados válidos" se ambos forem positivos ou 
# "Dados inválidos" caso contrário.

quantidade_usuario = int(input("Digite a quantidade: "))
preco_usuario = int(input("Digite o preço: "))

if quantidade_usuario > 0 and preco_usuario > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")
