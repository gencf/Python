T = [[1, 0, 1, 1], [0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 0, 1]]
#T = [1, 0, 0, 1, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [1, 1, 1, 0, 1], [0, 1, 0, 1, 1]]
n = len(T)

for i in range(n):
    for j in range(n):
        print(T[i][j], end="   ")
    print("\n")
is_sym = True

for i in range(n - 1):
    """
    if is_sym == False:
        break"""
    for j in range(n - i -1):
        if T[i][j] != T[j][i]:
            is_sym = False
        print(i, j, j, i, T[i][j], T[n-i-1][n-j-1], is_sym)
            
print(is_sym)
        
    