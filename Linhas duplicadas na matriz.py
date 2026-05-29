def verifica_linhas_iguais(matriz):
    linhas_vistas = {}
    
    for i, linha in enumerate(matriz):
        tupla_linha = tuple(linha) 
        
        if tupla_linha in linhas_vistas:
            linha_anterior = linhas_vistas[tupla_linha]
            print(f"=> Sim, as linhas {linha_anterior + 1} e {i + 1} são exatamente iguais.")
            return True
            
        linhas_vistas[tupla_linha] = i
        
    print("=> Não existem linhas duplicadas.")
    return False

# Exemplo de uso:
M2 = [
    [3, 9, 4, 2, 4, 1, 8, 5, 1], # Linha 1
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [3, 9, 4, 2, 4, 1, 8, 5, 1]  # Linha 3 (Igual à 1)
]
verifica_linhas_iguais(M2)
