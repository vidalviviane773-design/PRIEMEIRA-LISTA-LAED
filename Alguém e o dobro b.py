def alguem_e_dobro_ordenada(lista):
    esq = 0
    dir = 1

    while esq < len(lista) and dir < len(lista):
        if esq != dir and lista[dir] == 2 * lista[esq]:
            return True
        elif lista[dir] < 2 * lista[esq]:
            dir += 1
        else:
            esq += 1

    return False
