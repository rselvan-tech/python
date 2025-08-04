a = 1
b = ['a', 'b']
c = [10, 20]
def change():
    a = 66
    b.append(10)
    c = [100]
 
change()
print(a)
print(b)
print(c)