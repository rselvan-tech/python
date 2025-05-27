l1=[2,3,4]
print(l1,id(l1))

l1=l1+[5,6,7]
print(l1,id(l1))       #l1 address changed
'''
l1 + [5, 6, 7] creates a new list object.

Then = assigns this new list back to l1.

So the identity (id) changes because it’s a different object now.

💡 This is not an in-place update. It creates a new object and rebinds the name l1 to it.
'''

l1 +=[5,6,7]
print(l1,id(l1))       #l1 address not changed

'''
+= for lists is equivalent to calling l1.extend([5, 6, 7]).

This modifies the original list in place.

So the memory address (id) remains the same.

💡 This is an in-place operation because lists are mutable.
'''

l1.extend([45,55,36])  #extend adds items from the iterable to l1
l1 +=[5,6,7]
print(l1,id(l1))       #l1 address not changed


# extend vs append
list1=[2,3,4]
print(list1)               #[2, 3, 4] 

list1.append(['a','b'])    
print(list1)               #[2, 3, 4, ['a', 'b']]             <= adds the object arguement at the end

list1.extend(['x','y'])
print(list1)               #[2, 3, 4, ['a', 'b'], 'x', 'y']   <= adds the items from the iterable object arguement at the end

list1.append(20)           #[2, 3, 4, ['a', 'b'], 'x', 'y', 20]
print(list1)

list1.extend([20])         #[2, 3, 4, ['a', 'b'], 'x', 'y', 20, 20]
print(list1)

#list1.extend(20)           #TypeError: 'int' object is not iterable
