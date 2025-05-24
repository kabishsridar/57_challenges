euro_amount = float(input("How many euros are you exchanging? ")) # prompting the user for amount of euro 
exchange_rate = float(input("What is the exchange rate? ")) # prompting the user for exchange rate
usd = (euro_amount * exchange_rate) # as formula is mentioned in the question  amount to  = amount from * ratefrom / rate to

usd = round(usd) / 100 # Round up to the next penny

print(f"{euro_amount} euros at an exchange rate of {exchange_rate} is \n{usd} U.S. dollars.") # displaying the final output using single output statement
