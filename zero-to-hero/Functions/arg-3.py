def add(a, b=1, c):    #Syntax Error. Deafault arguments can't be follwed by a posional argument
    return a + b + c
 
print(add(10, 20, 30))