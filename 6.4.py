def find_zero(l):
    count = 0
    for i in l:
        try:
            find = 1/i
            count += 1
        except ZeroDivisionError:
            return count
    return -1

print(find_zero([1,2,3,4,5]))  
print(find_zero([123,35,0,46,2567]))
print(find_zero([0,1,0,1,1,0]))