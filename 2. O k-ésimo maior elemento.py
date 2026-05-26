def k_esimo_maior(lista, k):
    if k > len(lista) or k <= 0:
        return None
  
    lista_ordenada = sorted(lista, reverse=True)
    return lista_ordenada[k-1]
