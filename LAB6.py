def employee_info(a, b):
    a = a.split(",")
    b = b.split(",")
    info = ["Name","Surname","Age","Position","Employment Time"]
    employees = list()
    k = 0
    for i in a:
        i = i.split(" ")
        name = i[0]
        surname = i[1].upper()
        age = int(i[2])
        position = b[k]
        time = int(i[4])
        person = [name, surname, age, position, time]
        employee_info = dict(zip(info, person))
        employees.append(employee_info)
        k += 1
    return employees      
        
print(employee_info("Arthur MoRGaN 36 CEO 10,Josiah TrElAwNy 43 COO 12,John MaRSToN 33 Bookkeeper 8","Bookkeeper,CEO,COO"))






