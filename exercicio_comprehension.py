
# 1. Filtrando números pares em uma lista
# Exercício: Dada uma lista de números, crie uma nova lista 
# contendo apenas os números pares.

# numeros_gerais = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nova_lista = [n for n in numeros_gerais if n % 2 == 0]
# print(nova_lista)




# 2. Multiplicando cada número por 10
# Exercício: Dada uma lista de números, crie uma nova lista com cada 
# número multiplicado por 10.

# lista_numeros = [1, 3, 2, 5, 4, 66, 3, 90, 100, 33, 5, 7, 18]
# lista_nova = [n * 10 for n in lista_numeros]
# print(lista_nova)

# para cada n (numero da lista_numeros) multiplique por 10
# e vai fazenedo isso para cada n(numero) que tem na lista_numeros


# 3. Convertendo todas as palavras para maiúsculas
# Exercício: Dada uma lista de palavras, crie uma nova 
# lista com todas as palavras em letras maiúsculas.


# palavras = ['casa', 'carro', 'familia', 'filhos', 'amor', 'comida', 'alegria', 'paz']
# palavras_maiusculas = [p.upper() for p in palavras ]
# print(palavras_maiusculas)

# 4. Filtrando nomes com mais de 5 letras
# Exercício: Dada uma lista de nomes, crie uma nova lista 
# contendo apenas os nomes com mais de 5 letras.

# lista_de_nomes = ['Ana', 'Jordana', 'Gabriel', 'Maria', 'Joao', 'Arnaldo', 'Lorenzo', 'Benedita']
# Lista_maior_de_5 = [nome for nome in lista_de_nomes if len(nome) > 5]
# print(Lista_maior_de_5)


# 5. Extraindo os domínios de e-mails
# Exercício: Dada uma lista de e-mails, crie uma nova lista 
# contendo apenas o domínio dos e-mails (parte após o @).

# lista_de_emails = [ 'jornada@silva.com', 'gabriel@oliveira.silva', 'ana@balico.com', 'davi@anacleto.123']

# lista_de_dominio = [email.split("@")[1] for email in lista_de_emails]
# print(lista_de_dominio)

# 6. Filtrando números negativos
# Exercício: Dada uma lista de números, crie uma nova 
# lista contendo apenas os números negativos.

# lista_geral = [1, -3, -4, -67, -489, 0, -10, -345, -18, 3, 90, 89, 188, 26]
# lista_num_negat = [ n for n in lista_geral if n < 1]
# print(lista_num_negat)


# 7. Contagem de ocorrências de uma palavra em uma lista de strings
# Exercício: Dada uma lista de frases, crie uma nova lista 
# com a contagem de ocorrências da palavra "dados".

# lista_de_frases=['Tenho vários jogos de tabuleiro com dados','Quero ser engenheira de dados' ,'É preciso analisar os pontos de vistas e os dados','Eles estão jogando com dados viciados']

# lista_com_contagem = [elemento.lower().count('dados') for elemento in lista_de_frases]
# print(lista_com_contagem)

# 8. Filtrando números que são múltiplos de 3 ou 5
# Exercício: Dada uma lista de números, crie uma nova lista 
# contendo apenas os números que são múltiplos de 3 ou 5.

# numero_em_geral = [ 1, 3, 5, 6, 45, 34, 2, 33, 78, 90, 18, 55, 90, 100, 30, 66]
# numero_multiplos = [ n for n in numero_em_geral if n %3 == 0 or n % 5 == 0]
# print (numero_multiplos)


# 9. Extraindo o nome dos usuários de um dicionário de dados
# Exercício: Dado um dicionário contendo informações de usuários 
# (nome e email), crie uma lista com os nomes dos usuários.

info_usuarios = [
    {'nome': 'maria' , 'email' : 'maria@123'},
    {'nome': 'jose' ,'email' : 'jose@augusto'},
    {'nome' : 'nina' , 'email' : 'nina@menina'}
] 
lista_de_nomes = [ nome['nome'] for nome in info_usuarios]
print(lista_de_nomes)



# 10. Transformando uma lista de números em uma lista de quadrados
# Exercício: Dada uma lista de números, crie uma nova lista com 
# os quadrados desses números