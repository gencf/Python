f = open("deneme.txt","r+")
"""
line = f.readline()
while not line == []:
    values = [float(num) for num in line.strip("\n").split()]
    print(values, line)
    sum = 0
    for i in values:
        sum += i
    avg = sum/len(line)
    f.write("  " + str(avg))
    line = f.readline()
    print(f.tell())
"""
line = f.readline()
"""
while not line == "":
    print(line, f.tell())
    f.write("/")
    line = f.readline()"""
print(line)
f.close()


    
        
