def winner(nazif, osman):
    def divisor(n):
        counter = 0
        for i in range(1, n):
            if n % i == 0:
                counter += 1
        return counter
    if divisor(nazif) > divisor(osman):
        return "Nazif"
    if divisor(nazif) == divisor(osman):
        return "Draw"
    return "Osman"

print(winner(120, 144))
print(winner(191, 190))
print(winner(4, 121))