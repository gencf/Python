def satisfactory(file):
    with open(file, "r") as a:
        count = 0
        for i in a.readlines():
            s = [int(x) for x in i.strip("\n").split()]
            avg = s[0]*10/100 + s[1]*10/100 + s[2]*20/100 + s[3]*20/100 + s[4]*40/100
            if avg >= 60:
                count += 1
    return count

print(satisfactory("input_lab7.txt"))