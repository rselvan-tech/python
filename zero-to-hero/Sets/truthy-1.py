"""
In Python, various data types have "truthy" or "falsy" values when evaluated in a boolean context (like an if statement).

Empty collections (including empty sets, empty lists, empty tuples, empty dictionaries, and empty strings) are considered falsy.

Non-empty collections are considered truthy.
"""

digits = '0123456789'
name = 'Victor'
 
if set(name) & set(digits):
    print('AA')
else:
    print('BB')