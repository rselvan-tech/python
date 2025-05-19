digits = '0123456789'
x = digits[::-3]    # x is '9630'
print(x)
y = digits[:-1:-3]    # y is empty string
print(y)
'''
When using negative step (-3), slicing must start from a higher index and move to a lower index.
But digits[:-1:-3] tries to go backward from the beginning toward the end, which is invalid for a negative step — so it returns nothing.
'''
print('END')