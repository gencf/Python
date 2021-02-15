from math import *
import time

def my_sin(x):
    def fact(n):
        m = 1
        for i in range(1, n + 1):
            m *= i
        return m
    inf = 1e3
    k = 0
    sum = 0
    while k < inf:
        term = (-1)**k/fact(2*k+1)*x**(2*k+1)
        sum += term
        k += 1
    return sum

start = time.time()
print(my_sin(pi/4))
finish = time.time()
print(finish - start) 


def my_sin2(x):
    epsilon = 1e-12
    x_square = x*x
    term = x
    d = 1
    result = term
    while abs(term) > epsilon:
        term *= -x_square/((d + 1)*(d + 2))
        result += term
        d += 2
    return result

start = time.time()
print(my_sin2(pi/4))
finish = time.time()
print(finish - start)
