age = int(input("What is your age? ")) # prompting the user for age
driving_age = { # just to store the driving ages of various country
    "US" : 16,
    "IND" : 18,
    "CA" : 16,
    "MY" : 17
}
if age >= 18:
    print("You are eligible to drive in IND")
elif age >= 17:
    print("You are eligible to drive in MY")

elif age >= 16:
    print("You are eligible to drive in US and CA")

else:
    print("Enter a valid age")