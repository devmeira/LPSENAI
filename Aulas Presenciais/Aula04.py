# Aula 04

# Fazer Conta no GitHub

# Criar um arquivo lacos.py
# dar um print de print("Olá GitHub")

# ---- Segunda Parte da Aula ---- #

# sinal = input("Digite o sinal: ")

# if sinal == "vermelho":
#     print("PARE 🛑")
# elif sinal == "Amarelo":
#     print("AMARELO 🟡")
# else:
#     print("VERDE 🟢")

# ---- Exercícios ---- #
# Sistema de Login

# Usuário 
# Senha

# Dois inputs
# Teste Lógico -> Se usuário for igual ao usuário e senha que estiver na constante/variável vai funcionar.

senha = "1234"
usuario = "gatofelix"

usuarioDigitado = input("Digite o seu usuário: ").lower()
senhaDigitado = input("Digite o sua senha: ")

if usuario == usuarioDigitado and senha == senhaDigitado:
    print("Login Correto")
else:
    print("Login Incorreto")

# ---- 