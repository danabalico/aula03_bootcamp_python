### Desafio - Refatorar o projeto da aula anterior evitando Bugs!
CONSTANTE_BONUS= 1000

nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is not True:
    try:
        # 1) Solicita ao usuário que digite seu nome
        nome_usuario = input("Digite seu nome:  ")

        # PROBLEMAS QUE PODEM ACONTECER

        ## nao digitou nada
        if len(nome_usuario)== 0:
            raise ValueError ("Voce nao digitou nada")
            #exit() # para abortar o processo

        ## digitou um numero no lugar do nome
        elif  nome_usuario.isdigit(): # isdigit() é para ver se tem um digito
            raise ValueError ("O nome não deve conter números.")
            #exit() # para abortar o processo

        ## digitou só espaço
        elif nome_usuario.isspace():
            print("Você digitou só espaço")
            #exit()
        
        else:
            nome_valido = True
            print(nome_usuario, " é um nome válido")

    except ValueError as e:
        print(e)
        #exit()

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

while salario_valido is not True:
    try:
        salario_usuario = float(input("Digite o valor do seu salário: "))

        ## PROBLEMAS QUE PODEM ACONTECER: por ser float, já impede letras e espaços, se eu quiser o "len" tem que ser antes de ser float

        if salario_usuario < 0 :
            print("Por favor, digite um valor positivo para o salário.")
        
        else:
            salario_valido = True
            print("salário válido", salario_usuario)
    except ValueError as e:
        print(e)

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

while bonus_valido is not True:
    try:
        bonus_usuario = float(input("Digite o seu bonus: "))
        if bonus_usuario < 0:
            print("Por favor, digite um valor positivo para o bonus.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada invál;ida para o bonus. Por favor, digite um número. ")




# 4) Calcule o valor do bônus final
valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, 
# salário e bônus

print(f"O usuário {nome_usuario} possui o bonus de {valor_do_bonus}")
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?