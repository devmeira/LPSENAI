# === def Função === 

def se(condicao, valor_se_verdadeiro, valor_se_falso):
    
    return valor_se_verdadeiro if condicao else valor_se_falso 

alunos = [
    ("Meira", 40),
    ("Fudancio", 20),
    ("Gabriel", 33),
    ("Pedro", 40),
    ("Afonso", 66),
    ("Maria", 79)
]

print(f"{'Aluno':^15} {'Nota':^6} {'Situação':^12}")
print("-" * 38)

for nome, nota in alunos:
    situacao = se(nota >= 70, "APROVADO", se(nota >= 50, "RECUPERACAO", "REPROVADO"))

    print(f"{nome:13} {nota:>6} {situacao:^17}")

print("-" * 38)

print("\n --- Boletim ---")

aprovados = 0
recuperacao = 0
reprovados = 0

for nome, nota in alunos:
    situacao = se(nota >= 70, "APROVADO", se(nota >= 50, "RECUPERAÇÃO", "REPROVADO"))

    if situacao == "APROVADO":
        aprovados +=1
    elif situacao == "RECUPERAÇÃO":
        recuperacao +=1
    else:
        reprovados +=1

# Exibe o resultado

print(f"Total de APROVADOS: {aprovados}")
print(f"Total de RECUPERAÇÃO: {recuperacao}")
print(f"Total de REPROVADOS: {reprovados}")