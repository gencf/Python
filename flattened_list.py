def flatten(l):
    if len(l) == 0:
        return []
    if type(l[0]) != list:
        return l[:1] + flatten(l[1:])
    else:
        return flatten(l[0] + l[1:])
    
print(flatten(["f",[54], [234, [[[]]], "a", [4, True, [5, 6], 67, 8], 1], 2]))    
print(flatten([1, [4, 5, [6]], [["test"], 89], 6]))          


