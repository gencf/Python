def reinstall(s):
    d = {}
    l = s.strip("|").split("|=|")
    
    print(l)
    for i in l:
        p = i.split(":")
        name = p[0].strip().capitalize()
        number = int(p[1].strip())
        d[name] = number
        print(d)
    a = sorted(list(d.keys()))
    print(a)
    d1 = {}
    for j in a:
        d1[j] = d[j]
        
    return d1
    
print(reinstall("| ahmet : 16 |=| Mehmet : 19 |=| selin : 32 |=| PINAR : 8 |"))
print(reinstall("| SiLa : 2 |=| AbDuLlAh : 28 |=| PeLIN : 49 |=| PolaT : 99 |"))