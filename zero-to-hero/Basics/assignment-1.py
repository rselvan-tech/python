# Assignment is always 'by reference' in Python — you're assigning a name to point to an object.
# But the visible behavior depends on whether the object is mutable or immutable.

"""
1. Everything in Python is an object
Variables are names bound to objects, not containers holding values.

2. Assignment creates a reference to the object
When you do a = b, you're making a refer to the same object that b refers to.
"""

# *************Assignment with Immutable object******************
print(" *************Assignment with Immutable object****************** ")
a = 10
b = a
print(a)  # 10 
print(b)  # 10
print(" b 'is' a ( before ): " + str ( b is a)) # Output: True

b += 1

print(a)  # 10 — 'b' now refers to a different int object
print(b)  # 11
print(" b 'is' a ( After ): ", b is a) # Output: False

print(" *************Assignment with Mutable object****************** ")

l1 = [1, 2, 3]
l2 = l1  # l2 points to the same list object as l1
print(l1)  
print(l2) 
print("l2 'is' l1 (before): " + str(l2 is l1))  # Output: True

l1.append(4) 

print(l1)  
print(l2)  
print("l2 'is' l1 (after): " + str(l2 is l1))   # Output: True
