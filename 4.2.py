def decipher(t, s):
    for i in s:
        t = t.replace(i[0], i[1])
    return t

print(decipher("H45k3ll 15 4 g3n3r4l-purpo53, 5t4t1c4lly typ3d, pur3ly funct1on4l progr4mm1ng l4ngu4g3 w1th typ3 1nf3r3nc3 4nd l4zy 3v4lu4t1on.", [("3", "e"), ("4", "a"), ("5", "s"), ("1", "i")]))
print(decipher("APL (nam3d af73r 7h3 b00k A Pr0gramming Languag3) is a pr0gramming languag3 d3v3l0p3d by K3nn37h 3. Iv3rs0n. I7s c3n7ral da7a7yp3 is 7h3 mul7idim3nsi0nal array.", [("7", "t"), ("3", "e"), ("0", "o")]))