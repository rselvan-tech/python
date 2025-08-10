def calculate(x,y,/,operation="add"):
    if(operation=="add"):
        return x+y
    elif(operation=="multiply"):
        return x*y

print(calculate(5,3,operation="multiply"))