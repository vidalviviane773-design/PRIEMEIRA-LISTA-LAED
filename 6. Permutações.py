from collections import Counter

def sao_permutacoes(U, V):
    if len(U) != len(V):
        return False
        
    return Counter(U) == Counter(V)
