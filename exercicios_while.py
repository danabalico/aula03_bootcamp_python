### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave 
#específica ("sair") seja fornecida.

# dados = [] # fazer uma lista vazia
# input_usuario = "" # iniciamos a variavel para nao dar erro no loop
# while input_usuario.lower() != 'sair':
#     input_usuario = input("Digite um valor ( ou 'sair' para terminar): ")
    

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de 
#um intervalo específico até que a entrada seja válida.

# numero = int(input("Digite um número entre 0 e 10: "))

# while numero < 0 or numero > 10:
#     print("Número fora do intervalo!")
#     numero = int (input("Por favor, digite um número entre 0 e 10: "))

# print("Dados válidos") # se nao entrar no while vai mostrar isso

    

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, 
#onde cada "página" de dados é processada em loop até 
#que não haja mais páginas.

# pagina_atual = 1
# paginas_totais = 3

# while pagina_atual <= paginas_totais:
#     print(f"Processando a página {pagina_atual} de { paginas_totais}")
#     pagina_atual +=1

# print ("Todas as páginas foram processadas")




### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um 
#limite máximo de tentativas.

# tentativa_atual = 1
# num_max_tentativas = 10

# while tentativa_atual <= num_max_tentativas:
#     print(f"Estamos na tentativa {tentativa_atual} de {num_max_tentativas} para reconexão ")
    
#     # if True: # caso tenha reconectado
#     #     print("Conexão bem sucedida")
#     #     break
#     tentativa_atual +=1
# else: 
#     print(f"Falha ao conectar após { num_max_tentativas} tentativas")


### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor 
#específico que indica a parada.

lista_de_itens = [1, 2, 'stop', 18, 9]

contador = 0
while contador < len(lista_de_itens): # ou seja, enquanto ele nao tiver
#passado item a item da lista_de_itens
    if lista_de_itens[contador] == 'stop':
        print(f"Parada encontrada -> {lista_de_itens[contador]} <- encerrando o processamento. ")
        break
    # processa o item
    print(f"Processando item: {lista_de_itens[contador]}")
    contador +=1

    # aqui o sistema lidou com a paragem primeiro, depois incrementou
