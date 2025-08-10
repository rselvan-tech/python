#No statement is executed after the 'return' keyword.'return' exits the function
def my_func(x):
    x += 3
    return x
    print(f'x is {x}')
 
 
my_func(2)