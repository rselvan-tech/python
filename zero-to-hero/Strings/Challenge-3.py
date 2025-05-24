'''
Challenge #3

Write a Python script that converts foot [ft] to centimeter [cm]. 1 ft = 30.48 cm

The user will be prompted to enter the value in ft.

Display the value in cm with 2 decimals, formatted using an f-string.

Are you stuck? Do you want to see the solution to this exercise? Click here.
'''

feet=int(input("Enter Feet to convert : "))
cm=feet*30.48
print(f'Equivalent CM value : {cm:.2f}')