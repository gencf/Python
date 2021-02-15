def int_to_bin(x):
    l = str()
    while x > 0:
        a = x % 2 
        x = x // 2
        l = str(a) + l
        
    return "".join(l)
           
print(int_to_bin(18))       


def bin_to_int(x):
    l = list(str(x))
    sum = 0
    i = 0
    while i < len(l):
        if i == len(l) - 1:
            sum += int(l[i])
            return sum
        sum = (sum + int(l[i])) * 2
        i += 1

print(bin_to_int(10010))


def bin_to_int2(x):
    sum = 0
    l = list(str(x))
    for v in l:
        sum = sum * 2
        sum = sum + int(v)
    return sum

print(bin_to_int2(10010))     
    

