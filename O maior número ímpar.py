def maior_impar(lista):
    maior = float('-inf')
    for num in lista:
        if num % 2 != 0 and num > maior:
            maior = num

    return maior if maior != float('-inf') else None

V = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]
print("Maior ímpar:", maior_impar(V))
