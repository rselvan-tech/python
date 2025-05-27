l1=[4,5.6,'Python',True,[200,400,600],(1,2,3)]
print(l1)              #[4, 5.6, 'Python', True, [200, 400, 600], (1, 2, 3)]
print(len(l1))         #6
print(l1[5])           #(1, 2, 3)
print(l1[-1])          #(1, 2, 3)

l2=[]                  #Empty List
l3=list()              #Empty List
print(l2,l3)           #[] []

l1[3]=False            #List is Mutable
print(l1)              #[4, 5.6, 'Python', False, [200, 400, 600], (1, 2, 3)]

l4=list('Python')
print(l4)              #['P', 'y', 't', 'h', 'o', 'n']

l4.append(200)         #List is Mutable
print(l4)              #['P', 'y', 't', 'h', 'o', 'n', 200]

l4[3]=5                #List is Mutable
print(l4)              #['P', 'y', 't', 5, 'o', 'n', 200]



