# Truthy Values = any integer or flot ( other than 0,0.0), non empty string
# Falsy Values = 0, 0.0 , Empty string
# use bool() function to check truthy/Falsy values
# bool(0.0), bool('Hello')


print('Enter your name : ')
name=input()
if name:
    print("Thank you for entering your name")
else:
    print("You did not enter your name")