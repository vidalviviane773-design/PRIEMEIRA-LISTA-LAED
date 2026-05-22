def impar_frequencia_impar(lista):
    frequencias = {}

    for num in lista:
        if num % 2 != 0:
            frequencias[num] = frequencias.get(num, 0) + 1

    for num, freq in frequencias.items():
        if freq % 2 != 0:
            return f"Sim, o {num}"

    return "Não encontrado"

V = [9, 2, 77, 2, 2, 1, 7, 7, 9]
print("Ímpar com frequência ímpar:", impar_frequencia_impar(V))
