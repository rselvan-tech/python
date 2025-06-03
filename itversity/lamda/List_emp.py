employees=[
(1,'scott','tiger',1000.0,'USA'),
(2,'boott','abcd',300.0,'Canada'),
(3,'ttttt','tir',1200.0,'Mexico'),
(4,'scooo','aaa',500.0,'USA'),
(5,'coope','tig',100.0,'Italy'),
]

print(f'{type(employees)=}')
print(f'{len(employees)=}')

#Add elements

employees.append((6,'Donald','Duck',1275.0,'UAE'))
employees.insert(3,(7,'Micky','Mouse',275.0,'Canada'))

print(f'{len(employees)=}')
print(f'{employees=}')

#Delete elements
print(employees.pop())
print(f'{len(employees)=}')
print(f'{employees=}')

print(employees.pop(3))
print(f'{len(employees)=}')
print(f'{employees=}')

'''
employees.clear()
print(f'{len(employees)=}')
print(f'{employees=}')
'''

#Sorting
#help(list.sort)
#help(sorted)
employees.sort(key=lambda t: t[3])
print(f'{len(employees)=}')
print(f'{employees=}')
print(sorted(employees,key=lambda t: t[0], reverse=True))
#print(f'{len(employees)=}')
#print(f'{employees=}')