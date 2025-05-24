import math
order_amount = float(input("What is the order amount? "))
state = input("What is the state? ")
tax_rate = 0.055
tax = 0
subtotal = order_amount
states = "WISCONSIN RESIDENTS"
if state.lower() == "wi" or state.upper() == states:
    tax = math.ceil(order_amount * tax_rate * 100) / 100  # Round up to nearest cent
    subtotal = order_amount
total = order_amount + tax

if state.lower() == "wi" or state.upper() == states:
    print(f"The subtotal is ${subtotal}.\nThe tax is ${tax}.")
print(f"The total is ${total}.")
