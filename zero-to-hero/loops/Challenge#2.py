'''
Challenge #2

Write a Python program to check if an integer (x) is the power of another integer (y). Prompt the user to input both integers.

Input: 16, 2

Output: 2 ** 4 = 16

Are you stuck? Do you want to see the solution to this exercise? Click here.
'''

x=int(input('Input num1 : '))
y=int(input('Input num2 : '))

print(f"Input: {x}, {y}")
for n in range(1,x):
    if (z:= y ** n) == x:
        print(f'Output: {y} ** {n} = {z}')
        break
else:
    print(f'{x} is not the power of {y}')