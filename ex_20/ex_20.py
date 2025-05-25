import math

order_amount = float(input("What is the order amount? "))
state = input("What state do you live in? ").strip().lower()

tax = 0.0

if state == "wisconsin" or state == "wi":
    county = input("What county do you live in? ").strip().lower()
    tax_rate = 0.05
    if county == "eau claire":
        tax_rate += 0.005
    elif county == "dunn":
        tax_rate += 0.004
    tax = math.ceil(order_amount * tax_rate * 100) / 100

elif state == "illinois" or state == "il":
    tax_rate = 0.08
    tax = math.ceil(order_amount * tax_rate * 100) /100

total = math.ceil((order_amount + tax )* 100) / 100

# Final output in a single statement
if tax > 0:
    print(f"The tax is ${tax}.\nThe total is ${total}.")
else:
    print(f"The total is ${total}.")
