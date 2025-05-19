l1 = [1, 2]
id1 = id(l1)
l1.append(100)
id2 = id(l1)
print(id1 == id2)

l2=l1
print(l2 is l1)