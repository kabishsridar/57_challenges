import math
order_amount = float(input("What is the order amount? "))
state = input("What is the state? ")
tax_rate = 0.055
tax = 0
subtotal = order_amount
if state == "WI":
    tax = math.ceil(order_amount * tax_rate * 100) / 100  # Round up to nearest cent
    subtotal = order_amount
total = order_amount + tax

if state == "WI":
    print(f"The subtotal is ${subtotal}.\nThe tax is ${tax}.")
print(f"The total is ${total}.")
