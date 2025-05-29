'''
Challenge #4

Write a Python script that tests if a string is a palindrome.

Are you stuck? Do you want to see the solution to this exercise? Click here.
'''
str1=input('Enter a String: ')
str2=str1[::-1]
print(f'{str1=}\n{str2=}')
if str1==str2:
    print(f'{str1} is a plaindrome')
else:
    print(f'{str1} is not a plaindrome')
