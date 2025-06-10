"""
Develop myReduce
****************
- Iterate thorugh elements
- Perform aggregation logic using the aregument passed.Argument should have necessary arithmetic logic 
- Return the aggregated result
"""

def myReduce(c,f):
    t=c[0]

    for e in c[1:]:
        t=f(t,e)
    return t

if __name__ == "__main__":
    l1=list(range(1,10))

    sum=myReduce(l1, lambda a,b: a+b)
    print(f'{sum=}')

    mul=myReduce(l1, lambda a,b: a*b)
    print(f'{mul=}')

    low=myReduce(l1, lambda a,b: a if a<=b else b)
    print(f'{low=}')

    high=myReduce(l1, lambda a,b: max(a,b))
    print(f'{high=}')



