'''
Challenge #3

Write a Python program that counts and displays the vowels of a given string ignoring the letter case.

Input str: Hello Everybody!

Output: 5
'''

str1=input('Enter a String: ')

count=0
for c in str1.lower():
    if c in 'aeiou':
        count+=1

print(f'Output: {count}')
