def sumOfIntegers(lb,ub):
    total=0
    for i in range(lb,ub+1):
        total += i
    return total

def sumOfSquares(lb,ub):
    total=0
    for i in range(lb,ub+1):
        total += i*i
    return total

def sumOfCubes(lb,ub):
    total=0
    for i in range(lb,ub+1):
        total += i*i*i
    return total

def sumOfEven(lb,ub):
    total=0
    for i in range(lb,ub+1):
        total += i if i%2 == 0 else 0
    return total

print(sumOfIntegers(1,10))
print(sumOfSquares(1,10))
print(sumOfCubes(1,10))
print(sumOfEven(1,10))