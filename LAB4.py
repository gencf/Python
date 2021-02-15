def prefix(lst):
    def calculate(opt, a, b):
        if opt == "+":
            return a + b
        elif opt == "-":
            return a - b
        elif opt == "*":
            return a * b
    n = len(lst)
    result = 0
    for i in range(n // 2, n):
        if i == n - 1:
            return lst[i]
        result = calculate(lst[i - n // 2], lst[i], lst[i + 1])
        lst[i + 1] = result
        
print(prefix(["+", "*", "-","*", "+", 1, 2, 9, 3, 5, 12]))       
            