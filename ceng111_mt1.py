# 60
def f(x):
    x[:] = x[::-1]    
def g(x):
    x = x[::-1]   
def h(x):
    return x[::-1]
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst3 = [1, 2, 3]
f(lst1)
g(lst2)
h(lst3)
print(lst1, lst2, lst3)


# 61
"""def f(L, m):
    i=0
    j=len(L)-1
    k = (i+j)/2
    while not (L[k] == m or i>j):
        if m>L[k]:
            i=k+1
        else:
            j=k-1
            k = i +(j-i)/ 2
    return k
print(f([14, 21, 12, 38, 7, 8, 10, -2, 16, 32, 42, 0, 23], 21))"""


# 62
m = 0
def f(n):
    return g(n)+g(n+2)
def g(n):
    global m
    m = m + 1
    if n <= 1:
        return n
    else:
        return g(n-1)+g(n-2)
print(f(3), m)


# 63
print(int(int( 4 / 2.1 ) / 5 + float(4/5) + 7 + (3.6 + 5/8)))   


# 64
def f():
    def g():
        print("fg")
    print ("f")
    g()
def g():
    def f():
        print ("gf")
    print ("g")
    f()
g()
f()


# 65
"""def min(L):
    m = L[0]
    for i in range(len(L)):
        c = L.pop()
        if c < m:
            m = c
    return m
def max(L):
    m = L[0]
    for i in range(len(L)):
        c = L.pop()
        if c > m:
            m = c
    return m
L = [3, 2, -10, 5]
minimum = min(L)
maximum = max(L)
print (minimum, maximum)
# List index out of range error"""


# 66
"""def min1(L):
    m = L[0]
    length = len(L)
    i = 0
    while i < length:
        if L[i] < m:
            m = L[i]
    return m
def min2(L):
    m = L[0]
    i = 0
    while i < len(L):
        if L[i] < m:
            m = L[i]
    return m
print(min1(lst1), min2(lst2))"""


# 67
def f(N):
    return N if N == 0 or N == 1 else (True if not f(N-1) else False)
print(f(0), f(1), f(2), f(3), f(4), f(5), f(6), f(7), f(8), f(9))