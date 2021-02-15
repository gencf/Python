def maximum_occurrence(l):
    d = {}
    for i in range(len(l)):
        if l[i] in d:
            continue
        count = l.count(l[i])
        d[l[i]] = count
    max = 0
    a = 0
    for j in d:
        if d[j] > max:
            max = d[j]
            a = j
    return a
        
print(maximum_occurrence([1,1,1,0,4,4]))        
print(maximum_occurrence([0,3,3,3,1,0]))       

