my_str = 'I Love Python!'
 
if my_str[-2].islower() and 'Java' not in my_str:
    print(my_str[2:].upper())
elif my_str[::] != my_str:
    print(my_str.lower())
else:
    print(my_str[::-1])