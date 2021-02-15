def search(a, x):
    try:
        i = a.index(x)
    except ValueError:
        i = None
    return i

