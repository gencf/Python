"FURKAN GENC"
def buy_hats(a, money, number=0):
    a = sorted(a)
    if money <= 0 or len(a) == 0:
        return number
    if money >= a[0]:
        money -= a[0]
        number += 1
    return buy_hats(a[1:], money, number)

print(buy_hats([12, 3, 7, 5, 4, 8], 1200))
print(buy_hats([4, 3, 6, 2, 5, 5], 27))

"MEHMET TEKIN ULAS"
def buy_hats2(a, b):
    a = sorted(a)
    if b < a[0]:
        return 0
    else:
        return 1 + buy_hats(a[1:], b - a[0])

print(buy_hats2([12, 3, 7, 5, 4, 8], 1200))
print(buy_hats2([4, 3, 6, 2, 5, 5], 27))
a = [1]
print(a[5:])