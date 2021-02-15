def only_numbers(lst, n = 0):  # WITH RCCURSION
    if n >= len(lst):
        return lst
    if type(lst[n]) != int:
        lst.pop(n)
        return only_numbers(lst, n)
    return only_numbers(lst, n + 1)

print(only_numbers([10, "ali", [20], True, 4]))

def only_numbers2(lst):
    new_lst = []
    for i in lst:
        if type(i) == int:
            new_lst.append(i)
    return new_lst

print(only_numbers2([10, "ali", [20], True, 4]))
