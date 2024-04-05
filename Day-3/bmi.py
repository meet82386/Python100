height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bmi = weight / height ** 2

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Slightly overweight")
elif bmi < 35:
    print("Obese")
else:
    print("Clinicly obese")