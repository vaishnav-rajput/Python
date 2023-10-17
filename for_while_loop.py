for i in range(10):
    print(i) #prints 0 to 9
#range can take these parameters => start , stop, step    
# if there's one argument in range that means it's telling when to stop 
# if two then start, stop => for i in range(1,10) => stop at 10 but not include 10
# if three then third argument defines how much to increment by 

#can iterate through list too
x = [3,4,5,6,7,8]
for i in range(len(x)):
    print(x[i])

for i, element in enumerate(x):
    print(i, element) #prints out the index and value in x list
    

     