def contar_inversoes(lista):
    inversoes = 0
    n = len(lista)

    for i in range(n):
        for j in range(i + 1, n):
            if lista[i] > lista[j]:
                inversoes += 1

    return f"{inversoes} inversões"

V = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]
print(contar_inversoes(V))
