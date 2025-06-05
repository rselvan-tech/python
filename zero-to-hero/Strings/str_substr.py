'''
1. in operator
==============
Checks if a substring exists inside another string, returns True or False.
'''
text = "Hello, world!"
if "world" in text:
    print("Found substring")

'''
2. str.find(substring)
=======================
Returns the lowest index of the substring if found, else returns -1.
'''
text = "Hello, world!"
pos = text.find("world")
print(pos)  # Output: 7

pos = text.find("python")
print(pos)  # Output: -1


'''
3. str.index(substring)
======================
Like find(), but raises ValueError if substring not found.
'''
text = "Hello, world!"
pos = text.index("world")  # 7

#pos = text.index("python")  # Raises ValueError


'''
4. str.startswith(prefix)
=========================
Checks if string starts with substring, returns True or False.
'''
text = "Hello, world!"
print(text.startswith("Hello"))  # True
print(text.startswith("world"))  # False


'''
5. str.endswith(suffix)
=========================
Checks if string ends with substring.
'''
text = "Hello, world!"
print(text.endswith("!"))  # True
print(text.endswith("world"))  # False


'''
6. Using re module (regular expressions)
=======================================
If you want pattern-based searching:
'''

import re

text = "Hello, world!"
match = re.search(r"world", text)
if match:
    print("Found at position:", match.start())
else:
    print("Not found")

help(re.search)
help(match)

