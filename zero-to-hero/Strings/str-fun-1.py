# https://docs.python.org/3/library/stdtypes.html#string-methods
print(dir(str))              #print all the methods of 'str'
help(str.replace)            #help

s1='Python'
new_s1=s1.upper()
print(s1)                    #Python     Str is immutable
print(new_s1)                #PYTHON
print("ProgRAMMING".lower()) #programming

txt=':'.join('abc')
print(txt)