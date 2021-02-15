"""result += n[i][j] * m[j][k]
i,j row    len(n) 
j,k column len(n[0])

   j
   4 5 6
k  1 2 3

    j            k           k
i  1 2 3        1 4         a b
   4 5 6     j  2 5       i c d
                3 6
"""
def multiple(n,m):
    result = 0
    r = []
    for i in range(len(n)):
        r.append([])
        for k in range(len(m[0])):
            r[i].append(0)
    for a in range(len(r)):
        for b in range(len(r[0])):
            print(r[a][b],end="\t")
        print("\n")
        
    for i in range(len(m[0])):
        for k in range(len(n)):
            for j in range(len(m)):
                result += n[i][j] * m[j][k]
            r[i][k] = result
            for a in range(len(r)):
                for b in range(len(r[0])):
                    print(r[a][b],end="\t")
                print("\n") 
            result = 0
    return r  

print(multiple([[1,2,3], [4,5,6]], [[1,4], [2,5] ,[3,6]])) 
    
    
    


