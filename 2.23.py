number=int(input())
a=int(input())
b=int(input())
found = False
for i in range(number//a + 1):
    if found == True:
        break     
    for j in range((number-a*i)//b + 1):
        if a*i + b*j == number:
            print(i, j, a*i + b*j )
            found = True
            break
if found == True:
    print("YES")
else:
    print("NO")
           
