def verifica_elemento_duplicado(matriz):
    vistos = set()
    for i, linha in enumerate(matriz):
        for j, elemento in enumerate(linha):
            if elemento in vistos:
                print(f"=> Sim, o elemento {elemento} aparece mais de uma vez.")
                return True
            vistos.add(elemento)
            
    print("=> Não há elementos duplicados.")
    return False

M1 = [
    [3, 9, 4],
    [1, 2, 3],
    [5, 8, 2]
]
verifica_elemento_duplicado(M1)
