def calculate_cgpa(std):
    count = 0
    s = 1
    total = 0
    notfound = 0
    while s < 9:
        try:
            ort = get_gpa(std, s)
            total += ort
        except KeyError:
            notfound = 1
            break
        except ValueError:
            total += 1.0
        except IndexError:
            count += 1
        s += 1    
       
    if notfound:    
        return -1.0
        
    total_semester = 8 - count
    cpga = total / total_semester
    return round(cpga, 2)