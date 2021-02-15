def anagram(str1, str2):
    if str1 == str2:
        return False
    str1 = set(str1)
    str2 = set(str2)
    if str1 == str2:
        return True
    return False

print(anagram('hello', 'olla'))