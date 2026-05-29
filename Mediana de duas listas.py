def mediana_duas_listas(U, V):
    n = len(U)
    left, right = 0, n

    while left <= right:
        part_U = (left + right) // 2
        part_V = n - part_U
        max_left_U = float('-inf') if part_U == 0 else U[part_U - 1]
        min_right_U = float('inf') if part_U == n else U[part_U]

        max_left_V = float('-inf') if part_V == 0 else V[part_V - 1]
        min_right_V = float('inf') if part_V == n else V[part_V]

       
        if max_left_U <= min_right_V and max_left_V <= min_right_U:
            return (max(max_left_U, max_left_V) + min(min_right_U, min_right_V)) / 2.0
        
        elif max_left_U > min_right_V:
          
            right = part_U - 1
        else:
           
            left = part_U + 1

U = [1, 3, 6, 7, 10]
V = [11, 15, 17, 19, 21]
print("Mediana:", mediana_duas_listas(U, V))
