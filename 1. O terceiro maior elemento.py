def terceiro_maior(lista):
    if len(lista) < 3:
        return None 
    
    maior = segundo_maior = terceiro = float('-inf')
    
    for num in lista:
        if num > maior:
            terceiro = segundo_maior
            segundo_maior = maior
            maior = num
        elif num > segundo_maior and num != maior:
            terceiro = segundo_maior
            segundo_maior = num
        elif num > terceiro and num != segundo_maior and num != maior:
            terceiro = num
            
    return terceiro
