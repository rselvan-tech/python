'''
Challenge #2

Create a Python script that removes all the elements of a list that are duplicates.
'''

l1=[ 1,5,2,5,7,8,9,2,3,4,6,1,6,8,9]

l2=[]

for n in l1:
    if n not in l2:
        l2.append(n)


#l2=[n for n in l1 if n not in l2]

print(f'{l1=}\n{l2}')
