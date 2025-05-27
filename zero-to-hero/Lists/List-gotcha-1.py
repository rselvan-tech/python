print('####################### Assigment with Immutable(int)#########################')
num1=100
print(f'num1={num1},id={id(num1)}')

num2=num1
print(f'num2={num2},id={id(num2)}')

num1=500
print(f'num1={num1},id={id(num1)}')
print(f'num2={num2},id={id(num2)}')

print('####################### Assigment with Mutable(list)#########################')

l1=[10,20,30]
print(f'l1={l1},id={id(l1)}')

l2=l1
print(f'l2={l2},id={id(l2)}')

l1.append(1000)
print(f'l1={l1},id={id(l1)}')
print(f'l2={l2},id={id(l2)}')

print('#######################        Copy List             #########################')

l3=l1.copy()
print(f'l1={l1},id={id(l1)}')
print(f'l3={l3},id={id(l3)}')


l1.append(2000)
print(f'l1={l1},id={id(l1)}')
print(f'l3={l3},id={id(l3)}')


