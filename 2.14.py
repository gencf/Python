lst = list(input())
#print(lst)
n = len(lst)
result = []
count2 = 1
count = 1
i = 0
while i < n:
    
    temp = lst[i]
    for j in range(i+1,n):
        if lst[j] == temp:
            count += 1
            i += 1
        else:
            break
    result += str(count)
    result += temp
#   print(temp, count, count2,  result)
    i += 1
    count = 1

for i in result:
    print(i, end='')

print("furkan genc")