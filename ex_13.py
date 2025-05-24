import math

# Input
principal_amount = float(input("What is the principal amount? "))
interest_rate = float(input("What is the rate? "))
years = float(input("What is the number of years? "))
number_of_periods = float(input("What is the number of times the interest\nis compounded per year? "))

# Convert percentage rate to decimal
r = interest_rate / 100

# Compound Interest Formula
A = principal_amount * math.pow((1 + r / number_of_periods), number_of_periods * years)

# Round up to the next cent
A = math.ceil(A * 100) / 100

# Output
print(f"${principal_amount} invested at {interest_rate}% for {int(years)} years")
print(f"compounded {int(number_of_periods)} times per year is ${A}.")