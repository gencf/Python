""" STRING METHODS"""
s = "------kalem, --kitap, --defter------"
a = "ABCDE"
a1 ="AbCdE"
b = "12345"
c = " "
d = [a, b]
print(s.count('k', 0, 8)) 
print(s.find('kitap', 1, ))
print(a.isalnum());
print(a.isalpha()); 
print(b.isdigit()); 
print(s.islower())
print(a.isupper())
print(c.isspace())
print(a1.swapcase())
print(a.lower())
print(s.upper())

print(a.ljust(40,"#"))
print(a.rjust(40,"-"))
print(a.center(40))

print("-".join(a))
print(" # ".join(d))
print(s.lstrip("-"))
print(s.rstrip("-"))
print(s.strip("-"))
import re
print(re.sub("-","", s))
print(s.split(","))
print(s.split(",", 1))
print(s.partition(","))
print(s.replace(',', '/', 1).strip("-"))
print(s.strip("-").startswith("kalem"))
print(s.strip("-").endswith("p, defter"))


""" LIST METHODS"""
l = [1, 2, 3, 4, 5, "a", 2, "b", "c", "d"]
l.append("e"); print(l)
l.extend(["f"]); print(l)
print(l.count(2))
print(l.index(2, 5)) #5 is the starting index of search
l.insert(5, 6); print(l) #(index, x)
l.remove(2); print(l) #same as del l[l.index(x)]
del l[0]; print(l)
print("%d" %l.pop(5), l) # pop(i) is same as x = L[i]; del L[i]; return  x
l.reverse(); print(l)
l1=l[:6]; l2=l[6:] 
l1.sort(); l2.sort(reverse = True); print(l1, l2)


""" DICTIONARY METHODS"""
keys = [1,2,3,4,5]
value = ["a","b"]
values =  ["a","b","c","d","e"]
d = dict.fromkeys(keys,value); print(d)
d = dict(zip(keys, values)); print(d)
d0 = d.fromkeys(keys, value);print(d0)
d1 = {key: value for key in keys}; print(d1) 
d1.clear(); print(d1)
d2 = d.copy(); print(d2)
print(d.items(), d.keys(), list(d.values()))
print(d.__contains__(4), 4 in d)
d1.update(d); print(d1); # for k, v in d.items(): d1[k] = v
print(d.get(6, "no"), d, d.get(5, "no")) #d[k] if k in D, else "no"
print(d.pop(0, "KeyError")); print(d.pop(5), d)
print(d.popitem(), d); #Removes and returns an arbitrary (key, value) from d


" SET METHODS"
s1 = {1, 2, 3, 4}
s2 = {1, 2, 3, 4, 5}
s3 = {0, 1, 2, 3}
print(s1.issubset(s2)) #True if every element in T1 is in iterable T2
print(s2.issuperset(s1)) #True if every element in T2 is in iterable T1
s1.add(5); s2.add(5); print(s1, s2) #Adds element elt to set T (if it doesn’t already exist)
print(s1.remove(5), s1) #Removes element elt from set T. KeyError if element not found
s1.discard(5); print(s1) #Removes element elt from set T if present
print(s1.pop(), s1) #Removes and returns an arbitrary element from set T; raises KeyError if empty
s1.clear(); print(s1) #Removes all elements from this set
s1 = s3.copy(); s1.remove(3); s1.discard(5); s1.add(6); print(s1)
print(s1.union(s2, s3), s1 | s2 | s3, s1, s2, s3);
#Synonym to (T1 | T2). Returns a new Set with elements from either set  
print(s1.intersection(s2, s3), s1 & s2 & s3, s1, s2, s3)
#Synonym to (T1 & T2). Returns a new Set with elements common to all sets
print(s1.difference(s2, s3), s1 - s2 - s3, s1.difference(s2), s1 - s2, s1, s2, s3)
#Synonym to (T1 - T2). Returns a new Set with elements in T1 but not in any of T2
print(s1.intersection(s2), s1 & s2, s1.symmetric_difference(s2), s1 ^ s2, s1, s2)
#Synonym to (T1 ^ T2). Returns a new Set with elements from either of two sets but not in their intersection

"OTHER FUNCTIONS"

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8, 9]

# MAP: Returns the specified iterator with the specified function applied to each item
def f(x, y):
    return x*y
print(list(map(f, l1, l2)))
print(list(map(lambda x, y: x*y, l1, l2)))

# ZIP: Returns an iterator, from two or more iterators
d = dict(zip(l1, l2)); print(d)

# FILTER: Use a filter function to exclude items in an iterable object
print(list(filter(lambda number: number % 2 == 0, l1)))

# ITER and NEXT: Returns an iterator object / Returns the next item in an iterable
my_iter = iter(l1)
print(next(my_iter)); print(next(my_iter)); print(next(my_iter)); print(next(my_iter)); 

print("x{:10d}x\nx{:10}x\nx{:10.5f}x". format(1, "ali", 3.5))
