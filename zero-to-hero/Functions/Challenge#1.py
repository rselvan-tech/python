'''
Challenge #1

Write a Python function that takes a list as an argument and returns a new list with unique elements of the first list in the same order.

Sample List : [1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5]

Unique List : [1, 2, 3, 4, 5]
'''

def my_func( l1):
    s1=set(l1)
    l2=list(s1)
    return l2

list1=[1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5]
res=my_func(list1)
print(f'List ={list1}')
print(f'Set={res}')