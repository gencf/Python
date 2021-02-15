def ball_game(l, n):
    index = 0
    for i in range(n):
        try:
            next = l[index]
            index = next
        except:
            return index
    return index

print(ball_game([1, 3, 2], 1))
print(ball_game([1, 3, 2], 2))
print(ball_game([1, 3, 2], 3))
print(ball_game([3, 4, 5, 1, 2], 4))
print(ball_game([3, 4, 5, 1, 2], 5))
print(ball_game([3, 4, 5, 1, 2], 6))
print(ball_game([8, 7, 1, 5, 3, 10, 4, 2, 6, 9], 6))
print(ball_game([8, 7, 1, 5, 3, 10, 4, 2, 6, 9], 7))