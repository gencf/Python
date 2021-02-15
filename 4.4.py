def reverse_left(l, n):
    i = l.index(n)
    lsub = l[:i]
    rsub = l[i:]
    lsub.reverse()
    l = lsub + rsub
    return l

print(reverse_left([8,1,4,5,6,6,3,2], 6))
print(reverse_left([64, 51, 77, 34, 77, 39, 57, 67, 58, 63, 51], 39))