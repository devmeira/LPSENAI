### Estatisticas ###

def estatisticas(*numeros):
    total = sum(numeros)
    media = total / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    print(f"Total: {total} | Média: {media:.2f} | Máx: {maximo:.2f} | Mín: {minimo}")

estatisticas(59, 60, 80, 90, 46)
estatisticas(70, 89, 49)
#listas
lista = [80, 90, 95]
estatisticas(*lista)