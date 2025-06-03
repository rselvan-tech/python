def my_sum(lb,ub,f):
    total=0
    for i in range(lb,ub+1):
        total +=f(i)
    return total

def i(n): return n
def sqr(n): return n*n
def cube(n): return n*n*n
def even(n): return n if n%2 == 0 else 0

print(my_sum(1,10,i))
print(my_sum(1,10,sqr))
print(my_sum(1,10,cube))
print(my_sum(1,10,even))

print(my_sum(1,10,lambda n: n))
print(my_sum(1,10,lambda n: n*n))
print(my_sum(1,10,lambda n: n*n*n))
print(my_sum(1,10,lambda n: n if n%2 == 0 else 0))

