def func(x, y, z=None):
    return x * y, x/y #returns a tuple
result = func(1,2)
result1, resul2 = func(5,6)

def func(x):
    def func2():
        print(x)
    return func2        

func(3)() #prints 3
x = func(3)
x()#prints 3