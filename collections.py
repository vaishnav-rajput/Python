# list 
x = [4, True, 'hi']
length = len(x)
x.append('hello')
x.extend([4,5,6,7,78,'hi', True])
last_element = x.pop()
last_element_wd_index = x.pop(len(x) - 1)
access_element = x[2]
x[0] = 'hello'
x = [4, True, 'hi']
y = x[:] #x list is copied to y but as pass by value and not pass by reference


#tuples
x = (0, 0, 2, 2) #cannot be changed (immutable)

x = [[], () , [1, 2 , 'something'] , 'can store tuples and lists in a list']
