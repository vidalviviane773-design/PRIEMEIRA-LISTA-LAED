def busca_aproximada(lista, k):
    if not lista:
        return None

    mais_proximo = lista[0]
    menor_diferenca = abs(lista[0] - k)

    for num in lista:
        if num == k:
            return f"Encontrei o {k}!"

        diferenca = abs(num - k)
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            mais_proximo = num

    return f"Não está lá, mas eu encontrei o {mais_proximo}"

V = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]
print(busca_aproximada(V, 31))
