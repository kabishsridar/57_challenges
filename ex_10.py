subtotal = 0 # initiating subtotal as 0
for loop in range(3): # iterate 3 times to get price for 3 items
    price = float(input(f"Enter the price of item {loop + 1}: ")) # prompt user for price of item
    quantity = float(input(f"Enter the quantity of item {loop + 1}: ")) # prompt usre for number of items
    item_total = price * quantity # item_total will be the complete price of item
    subtotal += item_total # subtotal will be the total for all items
    tax = subtotal * 0.055 # tax rate mentioned 5.5% so multiplied by 0.55 to get tax
    total = tax + subtotal # grand total
print(f"SubTotal: ${subtotal}") # displaying output
print(f"Tax: ${tax}")
print(f"Total: ${total}")