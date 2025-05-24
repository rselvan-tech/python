'''
Challenge #1

Create a Python script that asks the user for a number and then prints out a list of all the divisors of each number less than the asked number.

Are you stuck? Do you want to see the solution to this exercise? Click here.
'''

num=int(input('Enter a number : '))

print('Devisors :',end=' ')
for n in range(1,num):
    if num % n == 0:
        print(n,end=' ')