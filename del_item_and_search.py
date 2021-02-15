def del_item(l, x):
    n = len(l)
    for i in range(x, n - 1):
        l[i] = l[i+1]
    return l[:-1]

print(del_item([0,1,2,3,4,5,6,7,8], 6))

def del_item2(l, x):
    return l[:x] + l[x+1:]

print(del_item2([0,1,2,3,4,5,6,7,8], 6))

def search(a, b):
    target = a
    source = b
    for i in range(len(source) - len(target) + 1):
        if source[i] == target[0]:
            found = True
            for j in range(1,len(target)):
                if source[i+j] != target[j]:
                    found = False
                    break
            if found == True: return [i, i+j]
    return False

print(search("ada", "abracadabra"))  


print(list(i*i for i in [0,1,2,3,4,5]))         
print([2*x+1 for x in [2,4,6,8]])    
print([x*y for x in [1,2,3] for y in [4,5,6]])
print([a+b for a in ["hello"] for b in "world"])
                    
             