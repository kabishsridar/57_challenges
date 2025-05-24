import math # importing math module for ceil and pow function

print("--- Reverse Compound Interest Calculator ---")
target_amount = float(input("What is your desired final amount? ")) # prompting user for inputs
rate = float(input("What is the interest rate (in %)? "))
years = float(input("What is the number of years? "))
compounds_per_year = float(input("How many times is the interest compounded per year? "))

# converting rate percentage to decimal
r = rate / 100

denominator = math.pow((1 + r / compounds_per_year), compounds_per_year * years)
principal_amount = target_amount / denominator
principal_amount = math.ceil(principal_amount * 100) / 100  # round up to next cent

# displaying the output
print(f"\nTo reach ${target_amount} at {rate}% interest over {int(years)} years,")
print(f"compounded {int(compounds_per_year)} times per year, you need to invest ${principal_amount}.")