def segundo_maior_impar(lista):
    maior = float('-inf')
    segundo_maior = float('-inf')

    for num in lista:
        if num % 2 != 0:
            if num > maior:
                segundo_maior = maior
                maior = num
            elif num > segundo_maior and num < maior:
                segundo_maior = num

    return segundo_maior if segundo_maior != float('-inf') else None


V = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]
print("Segundo maior ímpar:", segundo_maior_impar(V))
