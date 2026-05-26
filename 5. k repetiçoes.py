def possui_k_repeticoes(lista, k):
    frequencias = {}
    
    for num in lista:
        frequencias[num] = frequencias.get(num, 0) + 1
        if frequencias[num] >= k:
            return True, num
            
    return False, None
