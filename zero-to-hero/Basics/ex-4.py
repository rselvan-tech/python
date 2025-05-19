#Consider the following Python expression: a = 16 / 2 + 6 / 2 ** 2

#Add parenthesis to change the order of operations so that a is 1.0

'''
Here’s the relevant order of execution (from highest to lowest):

** (Exponentiation)

/ (Division)

+ and - (Addition and Subtraction)

Operators with the same precedence level are evaluated left to right, except for **, which is right to left.
'''

a = 16 / 2 + 6 / 2 ** 2
print(a)

a = 16 / (((2 + 6) / 2) ** 2)
print(a)