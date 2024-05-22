# BMI calculator

Weight = float(input("enter body's weight in pound : "))
height = float(input("enter height in cm : "))
Body_weight = Weight / 2.205
Change_height =  height / 100
BMI = round(Body_weight/(Change_height**2), 3)
print(int(BMI))

if BMI <= 18.4:
    print(f"your {BMI} is in underweight state.")
elif BMI <= 24.9:
    print(f"your {BMI} is in normal state.")
elif BMI <= 39.9:
    print(f"your {BMI} is in overweight state.")
else:
    print(f"your {BMI} is in obese")