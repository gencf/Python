from math import *

def f(x):
    return x**2 + 1

def integral(f, a, b, dx = 0.000001):
    x = a
    sum = 0
    while x < b:
        sum += ((f(x) + f(x + dx)) / 2) * dx
        x = x + dx
    return f"{sum:.5f}"

print(integral(f, 1, 4, 0.000001))
print(integral(sin, 0, pi, 0.000001))
print(integral(lambda x: sin(x)*x, 0, pi, 0.000001))