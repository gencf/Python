def average_weight(file):
    f = open(file, "r")
    lst = f.read().split()
    print(lst)
    sum = 0
    count = 0
    for i in lst:
        if 45 <= int(i) <= 125:
            sum += int(i)
            count += 1
    f.close()
    return sum / count

print(average_weight("input.txt"))