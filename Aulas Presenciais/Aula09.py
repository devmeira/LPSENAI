# Lista e Numero Aleatorio

# import random

# simbolos = ["🐂", "🐱‍👤", "🐱‍🚀", "☕", "🍊"]
# saldo = 20.0

# print("=== Kassinão do Senai ===\n")

# while saldo >= 2:
#     input("\nPressione ENTER para girar (custa R$ 2)...")
#     saldo -= 2

#     resultado = [random.choice(simbolos) for _ in range(3)]
#     print(" | ".join(resultado))

#     if resultado[0] == resultado[1] == resultado[2]:
#         premio = 20
#         saldo += premio
#         print(f"   JACKPOT!!! Você ganhou R$ {premio}!")

#     elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
#         premio = 5
#         saldo += premio
#         print(f" Ainda não, mas para ajudar vamos dar RS {premio}")

#     else:
#         print("Não foi dessa vez...")
#         print(f"Saldo atual: R$ {saldo:.2f}")

# Desafio Playlist 🎶🎶

# Criar uma lista no estilo playlist com 10 músicas
# Usar laços para exibir todas as músicas

playlist = ["Musica01", "Musica02", "Musica03", "Musica04", "Musica05", "Musica06", "Musica07", "Musica08", "Musica09", "Musica10"]

print("Essas são suas Playlists 🎶")

print("""
      01. Anos 2000;
      02. Melhores Animes;
      03. Lofi Chill
    """)

# Obs.: Não importa qual ele escolher vai abrir a mesma Playlist!

input("Digite qual playlist quer ouvir agora: ")

print("Segue as músicas da sua playlist escolhida!\n")

for _ in playlist:
    print(_)




