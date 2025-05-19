#BMI = weight(kg) / [Height(m)]2 kg/m²

weight=float(input("Enter weight in Kg : "))
height=float(input("Enter height in m : "))
bmi=weight / height ** 2

print("BMI : ", format(bmi,".2f"))