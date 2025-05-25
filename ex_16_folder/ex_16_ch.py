age = int(input("What is your age? ")) # prompting the user for age
driving_age = { # just to store the driving ages of various country
    "US" : 16,
    "IND" : 18,
    "CA" : 16,
    "MY" : 17
}

print("You are old enough to legally drive." if age >= 16 else "You are not old enough to legally drive.")
eligible_countries = [] # initiate eligible_countries as empty list
for country, minage in driving_age.items(): # loop through each items in dictionary
    if age >= minage: # if age is greater than or equal to the minage in dictionary
        eligible_countries.append(country) # add the country to eligible countries

if eligible_countries != []: # check if it is not empty and display the eligible countries
        print("Based on your age, you can legally drive in: " + ", ".join(eligible_countries))
else: # if it is empty, diplay you cannot legally drive
        print("Based on your age, you cannot legally drive in any of the listed countries.")