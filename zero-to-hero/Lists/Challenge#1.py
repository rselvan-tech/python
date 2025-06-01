"""
Challenge #1

Create a Python script that removes all the occurrences of a given element of a list.
"""
l1=[ 1,5,2,5,7,8,9,2,3,4,6,1,6,8,9]
remove=6
l2=[ n for n in l1 if n!= remove]
print(f'l1={l1}\n{l2=}')
