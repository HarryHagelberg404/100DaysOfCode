# Treasure Island
input_height = float(input("What's your height? (In meters please)\n"))
input_weight = int(input("What's your weight? (In kilograms please)\n"))

bmi = round(input_weight / input_height ** 2)

bmi = 36
print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("You are underweight")
elif bmi > 18.5 and bmi < 35:
    if bmi < 25:
        print("You have a normal weight")
    elif bmi > 25 and bmi < 30:
        print("You are overweight")
    else:
        print("You are obese")
else:
    print("You are clinically obese")
