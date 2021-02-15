climate = input()
lst = eval(input())

if climate == 'Polar':
    temp = -3
elif climate == 'Tropical':
    temp = 37
else:
    temp = 24.3

for i in lst:
    if int(i) > temp:
        print("U")
    else:
        print("F")
        