def reverse(lst, n = 0):
    if n == len(lst) // 2:
        return lst
    (lst[n], lst[len(lst) - 1 - n])  = (lst[len(lst) - 1 - n], lst[n])
    return reverse(lst, n + 1)
print(reverse([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))  
    
