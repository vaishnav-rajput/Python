hello = "tim"
world = "world"
hello = world
print(hello)
hello_world = "allowed" 

x = 'not changed'

def func(name):
    global x
    x = name

print(x)
func("changed")
print(x)