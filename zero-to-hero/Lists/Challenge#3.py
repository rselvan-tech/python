'''
Challenge #3

Consider the following string: nums = '10,20,30,40,50'

Create a Python script that creates a list of integers from the string.

The resulting list will be: [10, 20, 30, 40, 50]
'''
nums = '10,20,30,40,50'
l1=[int(n) for n in nums.split(',')]
print(f'{nums=}\n{l1=}')