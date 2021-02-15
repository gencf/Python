def reduce_number(x):
    sum = 0
    while x > 0:
        digit = x % 10
        x = x // 10
        sum += digit
    if sum // 10 > 0:
        return reduce_number(sum)
    return sum
        
print(reduce_number(589564123))   

