x = 2
def my_func():
    global x
    x = 3
    print(x)
 
 
my_func()
print(x)