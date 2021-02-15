def is_time_valid(t):
    if t.find('.') != 2 or len(t) != 5:
        return False
    time = t.split(".")
    for i in time:
        if i.isdigit() == False:
            return False
    if "00" < time[0] < "24" and "00" < time[1] < "60":
        return True
    else:
        return False
print(is_time_valid("23.20"))
print(is_time_valid("22.61"))
print(is_time_valid("ten past eleven"))