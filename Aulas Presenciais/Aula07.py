### Aula 07 ###

# LAÇOS LOOPS

# WHILE & FOR

# procurar = input("Pesquisar peça: ")
# estoque = ["Prego", "Porca", "Arruela", "Parafuso", "Mola"]

# for item in estoque:
#     if item == procurar:
#         print("Item encontrado no estoque!")
#         break # Interrompe o laço imediatamente
# else:
#     print("Item não encontrado após varredura completa.")

### WHILE

# nome = input("Digite o seu nome: ")

# while nome == "":
#     print("Você não digitou o seu nome")
#     nome = input("Por favor, digite o seu nome: ")

# print(f"Olá, {nome}! Tudo bem?")

### DESAFIO

# login = "meira"
# senha = "123"

# contador = 1

# while True:

#     loginUsuario = input("Login: ")
#     senhaUsuario = input("Senha: ")    

#     if login == loginUsuario and senha == senhaUsuario:
#         print("Você acessou o sistema")
#         break
#     else:
#         if contador != 3:
#             print("Login ou Senha incorretos, tenta novamente \n")
#         else:
#             break
#         contador += 1

# print("\nMuitas tentatívas erradas, de uma pausa e tome um café. Volte depois de alguns minutos")

### FOR - Explicar o que acontece!!
# contador = 0

# for i in range(100):
#     print(i)
#     contador += 1

# print(f"\n{contador}")

### Exemplo de Biblioteca IMPORT

# import random

# print("=== Adivinhe um número ===")

# secreto = random.randint(1, 100)
# tentativas = 0 
# palpite = 0

# while palpite != secreto:
    
#     palpite = int(input("Seu palpite (1-100): "))
#     tentativas += 1
    
#     if palpite < secreto:
#         print("Muito baixo!")
#     elif palpite > secreto:
#         print("Muito alto!")
#     else:
#         print(f"Parabéns! Acertou em {tentativas} tentativas")

### Lista Alunos

alunos = ["Meira", "Gabriel", "Bruno", "SENAI-Aluno", "Aluno01"]

for i in alunos:
    print(i)

# O "i" item é o item da lista que começa com "0" zero no Python então em quando o primeiro item 0 de aluno print depois o 1, depois o 2, o 3 e assim por diantes até o ultimo.
# Só não consigo entender como a função do for funciona quando é o i para ir até o final. 
# Ainda preciso internalizar melhor, compreender melhor!

# explicar porque funciona da seguinte maneira o código

# for alunos in alunos:
#     print(alunos)

# o "i" é uma variável de controle?

# Fazer com while ainda
# while true:
#     print(alunos[0])