def repetidos_proximos(lista, k):
    vistos_recentemente = {}
    
    for i, num in enumerate(lista):
        if num in vistos_recentemente and (i - vistos_recentemente[num]) <= k:
            return True, num
        vistos_recentemente[num] = i
        
    return False, None
