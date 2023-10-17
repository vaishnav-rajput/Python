# ==
# !=
# <=
# >=
# <
# >

print(ord('a')) #returns the ascii table value of the character 
print('ab' > 'ad')
#compares the ordinal values in order 

#conditional operators run after arithmetic operators
# and
# or
# not

x = 2
y = 3 
z = 4

result1 = x == y
result2 = x < y
result3 = result1 or not result2
#if result2 was True before it'll be converted to False first

#order of execution is 
#1-> not
# 2 -> and
# 3 -> or
 