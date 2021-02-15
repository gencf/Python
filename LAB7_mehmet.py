def satisfactory(input):
    count=0
    liste=[]
    input_file=open(input,"r")
    for line in input_file.readlines():
         sayılar= list(map(int,list(line.split())))
         quiz_notu=(sayılar[0]+sayılar[1])/10
         midterm_notu=(sayılar[2]+sayılar[3])/5
         final_notu=(sayılar[4]/100)*40
         toplam_not=quiz_notu+midterm_notu+final_notu
         liste.append(toplam_not)
    input_file.close()
    for toplam in liste:
        if toplam>=55:
            count+=1
    return count

print(satisfactory("input_mehmet.txt"))