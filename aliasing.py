a = "sa"
b = a
print(a, b)
print(id(a), id(b))
a = a +"as"
print(a, b)
print(id(a), id(b))


a = [1,2,3,4,5]
b = a
print(a, b)
print(id(a), id(b))
b.append(6); a.remove(5);
print(a, b)
print(id(a), id(b))


d1 = {1: 'a', 2: 'b',3: 'c'} 
d2 = d1
print( d1, d2)
print(id(d1), id(d2))
d1[4] = "d"
print( d1, d2)
print(id(d1), id(d2))


a = [1,2,3,4,5,6,7]
b = list(a)
c = a[:]
print(a,b,c)
print(id(a), id(b), id(c))
a[5:5] = [0]
print(a,b,c)
print(id(a), id(b), id(c))


l = [1, 4, -5, -10, -7, 3, 0]
print(l, id(l))

def min(L):
    print(L, id(L))
    m = L[0]
    for i in range(len(L)):
        c = L.pop()
        if c < m:
            m = c
    return m
print(min(l), l)

