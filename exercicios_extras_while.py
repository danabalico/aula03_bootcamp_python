# 1. Gerar IDs únicos para registros
# Enunciado:
# Você está trabalhando em um sistema que precisa gerar IDs únicos para um 
# conjunto de registros. Crie um programa que gere IDs começando de 1001 até 1010, 
# e armazene-os em uma lista.

ids = []
id_atual = 1001

while id_atual <= 1010:
    ids.append(id_atual)
    id_atual +=1
print("IDs gerados: " , ids )








