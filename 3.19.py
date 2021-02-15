def is_even(x):
    while x >= 1:
        x -= 2
    if x == 0:
        return True
    return False

print(is_even(69815))
