def mais_proximo_da_media(lista):
    if not lista:
        return None
    
    media = sum(lista) / len(lista)
    return min(lista, key=lambda x: abs(x - media))
