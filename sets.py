#no duplication of elements
x = set()
s = {4,34,3.2,3}
s.add(5)
s.remove(5)
print(4 in s) #checks if 4 is in s
s2= {3,4,5,55}
union_set = s.union(s2)
difference = s.difference(s2)
intersection = s.intersection(s2)