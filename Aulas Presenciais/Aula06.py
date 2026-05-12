### Aula 06 ###

# IF ELSE - Antes do Intervalo

# Calculadora Básica

# print("=== Calculadora ===\n")

# num1 = float(input("Digite o primeiro número: "))
# operador = input("Digite o operador: (+, -, /, *)")
# num2 = float(input("Digite o segundo número: "))

# if(operador == "+"):
#     print(num1 + num2)
# elif(num2 == 0):
#     print("Não é possível dividir um número por zero")
# elif(operador == "-"):
#     print(num1 - num2)
# elif(operador == "/"):
#     print(num1 / num2)
# elif(operador == "*"):
#     print(num1 * num2)
# else:
#     print("Não é um operador válido para a Calculadora Básica")

# Conversor de Peso - Modo Fazendeiro
print("=== Conversor de Peso (Kg ↔ Arroba) ===")

# peso = float(input("Digite o peso: "))
# unidade = input("É em K (quilos) ou A (arrobas)? ").upper()

# if unidade == "K":
#     arrobas = peso / 15
#     print(f"{peso} kg = {arrobas:.2f} arrobas")
# elif unidade == "A":
#     quilos = peso * 15
#     print(f"{peso} arrobas = {quilos:.2f} kg")
# else:
#     print("Unidade inválida!")

# LOOPS - Pós Intervalo

# while e for

procurar = input("Pesquisar peça: ")
estoque = ["Prego", "Porca", "Arruela", "Parafuso", "Mola"]

for item in estoque:
    if item == procurar:
        print("Item encontrado no estoque!")
        break # Interrompe o laço imediatamente
else:
    print("Item não encontrado após varredura completa.")