#Python provides multiple ways to format floats for printing or strings, 
# mainly using format() and f-strings.
x=3.14

print("{:.3f}".format(x))
print(f'{x:.3f}')

print("{:10.2f}".format(x))
print(f'{x:10.2f}')

print("{:010.2f}".format(x))
print(f'{x:010.2f}')

print("{:<10.2f}".format(x))
print(f'{x:<10.2f}')

print("{:.3e}".format(x))
print(f'{x:.3e}')