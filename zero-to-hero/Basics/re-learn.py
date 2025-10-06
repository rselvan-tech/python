a=10
b=3.14
c=True
d="Hello"
l=list(range(1,10))

print(f'{a=} {b=} {c=} {d=} {l=}')

print(type(a),type(b),type(c),type(d),type(l))

for a in range(1,100,5):
    print(a,end="  ")