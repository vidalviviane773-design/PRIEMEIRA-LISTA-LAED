def alguem_e_dobro_nao_ordenada(lista):
    vistos = set()
    for num in lista:
        if (num * 2 in vistos) or (num % 2 == 0 and num // 2 in vistos):
            return True
        vistos.add(num)
    return False
