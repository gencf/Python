def capitalize_sentences(t):
    for i in [".", "!", "?"]:
        t = t.split(i)
        for j in range(len(t)):
            t[j] = t[j].strip()
            if t[j] == "":
                t.pop(j)
                x = i
                continue
            t[j] = t[j][0].upper() + t[j][1:] 
        t = (i + ' ').join(t)
    return t + x 
              
print(capitalize_sentences('lorem. ipsum? dolor sit amet, consectetur! adipiscing elit.'))
a = capitalize_sentences('string methods are really useful in Python! you need to know them to succeed in CENG240.')
print(a, type(a))