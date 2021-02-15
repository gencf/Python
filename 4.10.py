def single_sorted_copy(l):
    lst = l
    for i in lst:
        value = i
        while lst.count(value) > 1:
            lst.remove(value)
    lst = sorted(lst) 
    return lst
            
print(single_sorted_copy([3, 3, 2, 2, 1, 1]))
print(single_sorted_copy([1, 3, 2, 2, 1, 1, 4]))