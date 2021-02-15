def is_perfect(x):
    lst = []
    sum = 0
    for i in range(1, x//2 + 1):
        if x % i == 0:
            lst.append(i)
    for j in lst:
        sum += j
    if sum == x:
        return True
    return False

print(is_perfect(28))