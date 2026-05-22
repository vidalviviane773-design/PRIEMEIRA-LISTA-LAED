def elementos_mais_proximos(lista):
    if len(lista) < 2:
        return None

    lista_ordenada = sorted(lista)
    menor_diff = float('inf')
    par = (None, None)

    for i in range(len(lista_ordenada) - 1):
        diff = abs(lista_ordenada[i] - lista_ordenada[i+1])
        if diff < menor_diff:
            menor_diff = diff
            par = (lista_ordenada[i], lista_ordenada[i+1])

    return f"os elementos {par[0]} e {par[1]}"

V = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]
print("Mais próximos:", elementos_mais_proximos(V))
