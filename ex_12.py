principal_amount = float(input("Enter the principal amount: ")) # prompt the user for principal amount
ROI = float(input("Enter the rate of interest (as a percentage): ")) / 100  # prompt the user for rate of interest and Convert to decimal
years = int(input("Enter the number of years: ")) # prompt the user for number of years


A = principal_amount * (1 + ROI * years) # A is the investment amount

# Round to two decimal places
A = round(A, 2)

# Displaying the output
print("After", years, "years at", round(ROI * 100, 1), "%, the investment will \nbe worth $", A)