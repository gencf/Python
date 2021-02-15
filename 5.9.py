def dice_game(file = "input5.9.txt"):
    f = open(file)
    p = f.readline().strip("\n").split()
    s = []
    w = []
    for i in p:
        s.append(0)
    line = f.readline()
    while line != "":
        line = [int(x) for x in line.strip("\n").split()]
        ws = max(line)
        n = line.count(ws)
        if n == 1:
            ns = 1
        elif n == 2:
            ns = 0.5
        elif n == 3:
            ns = 0.33    
        for i in range(len(line)):
            if line[i] == ws:
                s[i] += ns         
        line = f.readline()
    ws = max(s)
    for i in range(len(s)):
        if s[i] == ws:
            w.append(p[i])     
    w = ",".join(w) + " " + str(ws) 
    f.close()
    
    return "'" + w + "'" 
    
print(dice_game())  


