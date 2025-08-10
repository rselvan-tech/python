def my_func(a, b=2):
    a += b
    print(f'a is {a} and b is {b}')
 
 
 
my_func(3,4)      #Function call using "Positional arguments"
my_func(b=3,a=2)  #Function call using "Default arguments"
