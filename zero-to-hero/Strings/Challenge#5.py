'''
Challenge #5

Change the solution of the previous challenge so that both the white spaces and the 
letter case are ignored when checking if the string is a palindrome.
'''
str1=input('Enter a String: ')
tmp1=''.join(str1.split()).lower()
print(tmp1)
str2=tmp1[::-1]
print(f'{tmp1=}\n{str2=}')
if tmp1==str2:
    print(f'{str1} is a plaindrome')
else:
    print(f'{str1} is not a plaindrome')
