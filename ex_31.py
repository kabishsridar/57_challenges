def check_numbers(a): # check whether it is a number
    if a.isdigit():
        return True
    else:
        return False
age = (input("Age: ")) # prompt for age
resting_heart_rate = (input("Enter the resting pulse: ")) # prompt for resting_heart_rate
if check_numbers(age) and check_numbers(resting_heart_rate):
    age = int(age)
    resting_heart_rate = int(resting_heart_rate)
    print("-" * 25) # to display the box
    print("Intensity  |   rate")
    print("-" * 25)
    for intensity in range(55,100,5): # loop from 55 to 95 with step count 5
        intensity_decimal = intensity / 100 # converting percentage to decimal
        target_rate = (((220 - age) - resting_heart_rate) * intensity_decimal) + resting_heart_rate # by the given formula
        print(f"|{intensity}%        |   {round(target_rate)} bpm |")
    print("-" * 25)
else:
    print("Kindly enter the valid inputs(only numbers)")