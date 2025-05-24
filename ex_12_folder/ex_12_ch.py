# Prompt user for inputs
principal_amount = float(input("Enter the principal amount: "))
ROI = float(input("Enter the rate of interest (as a percentage): ")) / 100
years = int(input("Enter the number of years: "))

# Check if the input is valid
if isinstance(principal_amount, float):
    print("\nYearly breakdown of the investment:")

    for year in range(1, years + 1):
        A = principal_amount * (1 + ROI * year)  # Calculate investment amount per year
        A = round(A, 2)  # Round to two decimal places
        print(f"After {year} years at {round(ROI * 100, 1)}%, the investment will be worth ${A}")

    # Display the final amount
    print("Final Amount:")
    print(f"After {years} years at {round(ROI * 100, 1)}%, the investment will be worth ${A}")
else:
    print("Enter a valid number. Only numbers are accepted.")