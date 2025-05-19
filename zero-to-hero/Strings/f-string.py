fname,lname,age="John", "Smith", 45

print("Hello "+fname+' '+lname+"! You are "+str(age)+" years old")  # without f-string
print(f"Hello {fname} {lname}! You are {age} years old")            # with f-string

radius=4.5
PI=3.17
print(F"Circle area with a radius of {radius} is {PI * radius ** 2}")  # F-string print only value
print(F"Circle area with a radius of {radius} is {PI * radius ** 2:.2f}")  # F string print only value and format
print(F"Circle area with a radius of {radius=} is {PI * radius ** 2=}")  # F string print variable name with value




