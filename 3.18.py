def my_range(a, b, c, lst = []):
    if a+c > b:
        return lst
    lst.append(a)
    return(my_range(a+c, b, c, lst))
    
print(my_range(3, 10, 1))
