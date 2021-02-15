def postfix(lst):
    n = len(lst)    #listemizin eleman sayisi, ornegin n=7 olsun
    result = lst[0]   #islemlerimizin sonucunu tuttugumuz degisken, ilk islem icin lst[0] olarak atandi.    
    for i in range(1, n//2 + 1):   #lst listesindeki her bir sayıya karsilik gelen islemi yapabilmemizi saglayan dongu
        if lst[i + n//2] == '+':   #islemin indisi 1. indisteki sayi icin 1+3=4, 2. sayi icin 5, 3. sayi icin 6 olur. 
            result += lst[i]
        elif lst[i + n//2] == '*':   
            result *= lst[i]                               
        elif lst[i + n//2] == '//':   
            result //= lst[i]
    return result

print(postfix([1,2,9,4,'+','*','//']))