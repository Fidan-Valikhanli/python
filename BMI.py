weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))
height_meters = height / 100
bmi = weight / (height_meters ** 2)
print(f"Your BMI is: {bmi:.2f}")