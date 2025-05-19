movie='The GodFather'
l1=len(movie)
print(f'Length :{len(movie)}')

print('Index using while loop')
i=0
while i<l1:
    print(movie[i])
    i+=1

print('Index using for loop')
for j in range(0,l1):
    print(movie[j])

print('Index using for loop - reverse 1')
for k in range(l1-1,-1,-1):
    print(movie[k])

print('Index using for loop - reverse 2')
for l in range(-1,-14,-1):
    print(movie[l])


