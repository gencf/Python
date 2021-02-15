def readable(lst):
    for i in lst.split(","):
        print(i.lower().strip())
        
readable("LemOn,   gaRlic, PASta")
readable("CheeSe, cHeesE,    CHEESE")
