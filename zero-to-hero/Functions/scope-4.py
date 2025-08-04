x = 1
def func(x=0):
    x += 9
    return x
 
print(x, func(), func(10))