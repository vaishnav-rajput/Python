x = [1,2,3,4,5,6,7,8,9]

mp = map(lambda i:i + 2, x)
print(list(mp))

mp = filter(lambda i: i % 2 == 0, x) 
