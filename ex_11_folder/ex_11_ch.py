import math # import math module to use ceil function for rounding off

# conversion rates are taken from chatgpt
# Exchange rates (1 Euro to target currency), approximate values
conversion_rates = {
    "USD": 1.10,   # United States Dollar
    "GBP": 0.85,   # British Pound
    "INR": 89.70,  # Indian Rupee
    "JPY": 169.80, # Japanese Yen
    "CAD": 1.50,   # Canadian Dollar
    "AUD": 1.63,   # Australian Dollar
    "CHF": 0.97,   # Swiss Franc
    "CNY": 7.95,   # Chinese Yuan
    "SEK": 11.57,  # Swedish Krona
    "NZD": 1.76    # New Zealand Dollar
}

print("Available currencies:")
for country in conversion_rates: # displaying the currency codes to select the country using for loop
    print(f" - {country}")

# prompt the user for currency code
currency = input("Enter the target currency code (e.g., USD, GBP): ").upper()

# check whether the input is available in the dictionary
if currency in conversion_rates:
    euros = float(input("How many euros are you exchanging? ")) # if the currency code is available, then prompt for amount of euros to exchange
    rate = conversion_rates[currency]
    converted = math.ceil(euros * rate * 100) / 100  # round up to nearest amount
    print(f"{int(euros)} euros at an exchange rate of {rate} is {converted} {currency}.")
else:
    print("Sorry, that currency is not supported.")
