# def func(*args, **kwargs):
#     pass

x = [1,23,2345,3434]
print(x) #[1,23,2345,3434]
print(*x) # 1 23 2345 3434   => unpacked

def func(x,y):
    print(x,y)

pairs = [(1,2), (3,4)]

for pair in pairs:
    func(*pair) #will run the function for each tuple

func(**{'x': 2, 'y': 5})

func(1,2,3,4,5, one=0, two=1)


