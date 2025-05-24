import random
import string

length=int(input('Enter Pwd Length : '))
#help(string)


characters=string.ascii_letters+string.digits+string.punctuation

pwd=''

for _ in range(length):
    c=random.choice(characters)
    pwd+=c

print(f'Your passwprd is > {pwd}')

