weight = int(input("Enter your weight: ")) # prompt the use for inputs
gender = input("Enter your gender (M / F): ")
drinks = int(input("Enter the number of drinks: "))
A = int(input("the amount of alcohol by volume of the drinks consumed: "))
time = int(input("Enter the amount of time since your last drink in hours: "))
r = 0
if gender == "M":
    r = 0.73
elif gender == "F":
    r = 0.66
BAC_with_H = (A * (5.14/weight * r))
BAC = BAC_with_H - 0.015 * time # the final BAC calculated
print(f"Your BAC is {BAC}")
if BAC <= 0.08:
    print("You can drive")
else:
    print("its illegal for you to drive")