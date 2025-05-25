import math # import math module to use ceil

def calculateMonthsUntilPaidOff(b, apr_percent, p):
    # Convert APR percent to daily rate
    i = apr_percent / 100 / 365
    # Calculate the number of months using the formula
    numerator = math.log(1 + (b / p) * (1 - math.pow(1 + i, 30)))
    denominator = math.log(1 + i)
    n = - (1 / 30) * (numerator / denominator)
    # Round up to next whole month
    return math.ceil(n)

# Get inputs
b = float(input("What is your balance? "))
i = float(input("What is the APR on the card (as a percent)? "))
p = float(input("What is the monthly payment you can make? "))

n = calculateMonthsUntilPaidOff(b, i, p)
print(f"It will take you {n} months to pay off this card.")