def find_first_non_prime(lst):
    def is_nonprime(x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    for j in lst:
        if is_nonprime(j) == False:
            return j
    return False  
print(find_first_non_prime([2,3,4,7]))
print(find_first_non_prime([2,3,5,7]))
print(find_first_non_prime([2,3,51,19]))
