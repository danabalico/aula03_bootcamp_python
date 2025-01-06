# 1. Gerar IDs únicos para registros
# Enunciado:
# Você está trabalhando em um sistema que precisa gerar IDs únicos para um 
# conjunto de registros. Crie um programa que gere IDs começando de 1001 até 1010, 
# e armazene-os em uma lista.

# ids = []
# id_atual = 1001

# while id_atual <= 1010:
#     ids.append(id_atual)
#     id_atual +=1
# print("IDs gerados: " , ids )


# 2. Validar formatação de datas
# Enunciado:
# Implemente um programa que peça ao usuário para inserir uma 
# data no formato DD/MM/YYYY. O programa deve continuar pedindo 
# até que o formato correto seja digitado.

# aqui colocou a condição no while antes de colocar o input

# import re #biblioteca de extressoes regulares

# data_usuario = ""

# while not re.match (r"^\d{2}/\d{2}/\d{4}$", data_usuario): 
#     data_usuario = input ("Digite uma data no formato DD/MM/AAAA: ")

# print("Data válida inserida: ", data_usuario)

# 3. Monitorar tamanho de arquivos (Versão Júnior)
# Enunciado:
# Crie um programa que peça ao usuário para inserir os tamanhos 
# de arquivos (em MB). O programa deve parar de pedir tamanhos 
# quando o total de todos os tamanhos somados for maior que 500 MB. 
# No final, exiba o total e os tamanhos inseridos

tamanho_do_arquivo = []
tamanho_total = 0


while tamanho_total <= 500:
    try:
        tamanho = float(input("Digite o tamanho do seu arquivo: "))
        tamanho_do_arquivo.append(tamanho)
        tamanho_total+= tamanho
    except ValueError:
        print("Por favor, insira um número válido. ")

print(f"Tamanhos inseridos:{tamanho_do_arquivo}")
print(f"Total de tamanho dos arquivos : { tamanho_total : .2f} MB")
    

# explicação:
# vamos colocando os valores digitadoes em tamanho_do_arquivo
#criamos a variável "tamanho" para receber os valores
#a variavel "tamanho total" auxilia na soma 





