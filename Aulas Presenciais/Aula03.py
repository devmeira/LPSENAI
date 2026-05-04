# # Aula 03 - 13/04/26

# print("="*5, "🚨 Restaurante CódigoVermelho 🚨", "="*5)

# nome_cliente = input("Digite seu nome: ")

# print("Olá", nome_cliente, "seja bem vindo ao Restaurante CódigoVermelho")
# print("\n" + "="*30 + "\n")

# # Exibindo o Cardápio
# print("-"*8, "Cardápio", "-"*8)
# print("1. Hambúrgue Bug Simples         - R$ 25.00")
# print("2. Hambúrgue Bug Duplo           - R$ 35.00")
# print("3. Refrigerante Tela Preta       - R$ 08.00")
# print("4. Refrigerante Tela Laranja     - R$ 08.00")
# print("5. Sobremessa Bug Vermelho       - R$ 30.00")

# print("\n" + "="*25 + "\n")

# # Aqui começa o pedido
# print("Faça o seu pedido: ")
# qtd_hamburguer = int(input("Quantos Hamburgueres? "))
# qtd_refrigerante = int(input("Quantos Refrigerantes? "))
# qtd_sobremessa = int(input("Quantas Sobremessa? "))

# # Processar Valores
# valor_qtd_hamburguer = qtd_hamburguer * 25
# valor_qtd_refrigerante = qtd_refrigerante * 8
# valor_qtd_sobremessa = qtd_sobremessa * 30
# total_conta = valor_qtd_hamburguer + valor_qtd_refrigerante + valor_qtd_sobremessa

# # Cupom Fiscal
# print("="*20)
# print("="*7, "CUPOM", "="*7)
# print("="*20)
# print("Cliente:", nome_cliente)
# print(f"Valor dos Hamburgueres: {valor_qtd_hamburguer:.2f}")
# print(f"Valor dos Refrigerantes: {valor_qtd_refrigerante:.2f}")
# print(f"Valor das Sobremessas: {valor_qtd_sobremessa:.2f}")
# print("-"*20)
# print(f"Sua conta ficou: R$ {total_conta:.2f}")

# Boletim - Continuação Aula 03 - Condicional

nota_aluno = float(input("Informe a nota do aluno: "))

media = 7

if nota_aluno >= media:
    print("Aprovado")
elif nota_aluno >= 5:
    print("Recuperação")
else:
    print("Reprovado")