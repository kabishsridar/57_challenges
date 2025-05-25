height = float(input("Enter height in inches: ")) # prompt the user for height
weight = float(input("Enter weight in pounds: ")) # prompt the user for weight
bmi = (weight / (height * height ))* 703 # calculate bmi

# check the condition and display output
if bmi < 25 and bmi > 18.5:
    print("Normal weight")
elif bmi > 25:
    print("Overweight")
elif bmi < 18.5 and bmi > 0:
    print("Underweight")
else:
    print("enter valid integer")