def contem_elemento_isolado(lista):
    conjunto_elementos = set(lista)
    
    isolados = []
    for num in lista:
        if (num - 1) not in conjunto_elementos and (num + 1) not in conjunto_elementos:
            isolados.append(num)
            
    return len(isolados) > 0, isolados
