# IF e ELSE
# Hoje tivemos uma apresentação (Slides) - Utilizou o Notebook LM

# Está utilizando o IF e ELSE para falar de Booleanos
# print(10 < 5) - false
# print(10 > 5) - true
# print(10 >= 10) - true
# print(10 <= 5) - false
# print(10 != 5) - true
# print(10 != 10) - false
# print(10 == 10) - true

# idade = int(input("Digete sua idade: "))

# cnh = input("Tem CNH? (sim/não): ")

# if idade >= 18 and cnh == "sim":
#     print("Você pode dirigir")
# else:
#     print("Você não pode dirigir")

# estudante = True
# idoso = int(input("Digite idade: "))

# if estudante == True or idoso >= 65:18
#     print("Ganhou desconto")
# else:
#     print("Não foi dessa vez!")

idade = int(input("Digite sua idade: "))
condicaoFisca = input("Estado de saúde? (Boa/Ruim) ")
atestadoMedico = input("Tem atestado médico? (Sim/Não) ")

if idade >= 18 and (condicaoFisca == "Boa" or atestadoMedico == "Não"):
    print("Pode viajar")
else:
    print("Não pode viajar")