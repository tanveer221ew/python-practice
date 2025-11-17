# 2.	Create a BMI calculator
# BMI = weight/height
user_weight = float(input("Enter you weight in Kilograms"))
user_height = float(input("Enter you height in meters"))
userBMI = user_weight/user_height
if userBMI < 18.5:
    print("You are underweight")
elif userBMI <= 24.9 and userBMI >= 18.5:
    print("Your weight is normal")
elif userBMI >=25 and userBMI <= 29.9:
    print("You are overweight")
else:
    print("You are obsese")