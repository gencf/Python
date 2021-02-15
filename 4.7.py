def is_diagonal(m):
    n = len(m)
    for i in range(n):
        if m[i].count(0) != n - 1 or m[i][i] == 0 or type(m[i][i]) != int:
            return False
    return True

print(is_diagonal([[1,0,0],[0,1,0],[0,0,1]]))        
print(is_diagonal([[1,1,1],[2,4,0],[3,3,3]]))

def is_diagonal2(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            if i == j and (m[i][j] == 0 or type(m[i][j]) != int):
                return False
            if i != j and m[i][j] != 0:
                return False
    return True

print(is_diagonal2([[1,0,0],[0,1,0],[0,0,1]]))        
print(is_diagonal2([[1,1,1],[2,4,0],[3,3,3]]))


