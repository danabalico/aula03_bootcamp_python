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
# elif temp >= 18 and temp <= 26:# ou 18<= temperatura <=26:
#     print(f"{temp}°C é uma temperatura normal")
# else:
#     print(f"{temp}°C é uma temperatura alta")


# Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa 
# filtrar mensagens com severidade 'ERROR'. 
# Dado um registro de log em formato de dicionário 
# como log = {'timestamp': '2021-06-23 10:00:00', 
# 'level': 'ERROR', 'message': 'Falha na conexão'}, 
# escreva um programa que imprima a mensagem se a 
# severidade for 'ERROR'.

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 
#        'message': 'Falha na conexão'}
# if log ['level'] == 'ERROR':
#     print(log['message'])



# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um 
# sistema de recomendação, você precisa garantir que 
# cada usuário tenha idade entre 18 e 65 anos e 
# tenha fornecido um email válido. Escreva um 
# programa que valide essas condições e 
# imprima "Dados de usuário válidos" ou o erro específico encontrado.

# idade_usuario = int(input("Qual a sua idade? "))
# email_usuario = input("Qual o seu email? ")


## se o email e a idade forem fora do permitido:
## if (idade_usuario < 18 or idade_usuario >= 65) and ("@" not in email_usuario or "." not in email_usuario):
##    print("Idade fora do intervalo permitido e email inválido.")



# if idade_usuario < 18 or idade_usuario >= 65:# ou if not 18<= idade <=65
#     print("Idade fora do intervalo permitido")
# elif "@"not in email_usuario or "." not in email_usuario:
#     print("Email inválido")
# else:
#     print("Dados de usuário válidos")



# Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e 
# precisa identificar transações suspeitas. Uma transação é 
# considerada suspeita se o valor for superior a 
# R$ 10.000 ou se ocorrer fora do horário comercial 
# (antes das 9h ou depois das 18h). Dada uma transação 
# como transacao = {'valor': 12000, 'hora': 20}, verifique se 
# ela é suspeita.

# transacao = {'valor': 12000, 'hora': 20}

# if transacao['valor'] > 10000 or transacao ['hora'] < 9 \
#     or transacao['hora'] > 18:
#     print("Transação suspeita")
# else:
#     print("Transação normal")
    



