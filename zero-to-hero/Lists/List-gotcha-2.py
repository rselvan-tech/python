# remove all the numbers less than 5 from the list

l1=[2,55,4,67,55,78,3,22,4,88]
print(f'l1={l1}')
for n in l1:
    if n <=5:
        l1.remove(n)

print(f'l1={l1}')

l2 = [2, 4, 3, 1]
print(f'l2={l2}')
for n in l2:
    if n <= 5:
        l2.remove(n)
print(l2)


'''
⚠️ Why it's problematic
==========================
When you iterate over a list using a for loop, Python uses an internal index to go from item to item. If you change the list (e.g., add or remove elements) while iterating:

You can skip elements.

Or even get an IndexError in some cases.
'''

'''
1. Iterate over a copy
========================
nums = [1, 2, 3, 4, 5]
for num in nums[:]:  # iterate over a shallow copy
    if num % 2 == 0:
        nums.remove(num)
print(nums)
# Output: [1, 3, 5]

2. Use list comprehension (when filtering)
===========================================

nums = [1, 2, 3, 4, 5]
nums = [num for num in nums if num % 2 != 0]
print(nums)
# Output: [1, 3, 5]

3. Build a new list
====================
nums = [1, 2, 3, 4, 5]
new_nums = []
for num in nums:
    if num % 2 != 0:
        new_nums.append(num)
print(new_nums)

'''


