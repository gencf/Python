def sum67(n): #Verilen listedeki 6 sayisi, 7 sayisi ve arasinda kalan elemanlar haric diger elemanları toplar
    if n == []:
        return 0
    def find6(l):
        for i in range(len(l)):
            if l[i] == 6:
                return i
    def find7(start, l):
        for j in range(start + 1, len(l)):
            if l[j] == 7:
                return j
    sum = 0
    for k in range(len(n)):
        if k in range(find6(n), find7(find6(n), n) + 1):
            continue
        sum += n[k]    
    return sum
                
print(sum67([1,2,3,6,78,4,99,89,7, 5]))        

