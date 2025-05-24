age = int(input("What is your age? ")) # prompting the user for age
driving_age = { # just to store the driving ages of various country
    "US" : 16,
    "IND" : 18,
    "CA" : 16,
    "MY" : 17
}

print("You are old enough to legally drive." if age >= 16 else "You are not old enough to legally drive.")
eligible_countries = []
for country, minage in driving_age.items():
    if age >= minage:
        eligible_countries.append(country)

if eligible_countries != []:
        print("Based on your age, you can legally drive in: " + ", ".join(eligible_countries))
else:
        print("Based on your age, you cannot legally drive in any of the listed countries.")