#BMI

h = float(input("Height in m: "))
w = float(input("Weight in kg: "))

BMI = w / (h**2)

print("BMI is", BMI)

if BMI <= 18.4:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are overweight.")
else:
    print("You are obese.")