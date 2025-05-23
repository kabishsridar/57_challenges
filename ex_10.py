subtotal = 0
for loop in range(3):
    price = float(input(f"Enter the price of item {loop + 1}: "))
    quantity = float(input(f"Enter the quantity of item {loop + 1}: "))
    item_total = price * quantity
    subtotal += item_total
    tax = subtotal * 0.055
    total = tax + subtotal
print(f"SubTotal: ${subtotal}")
print(f"Tax: ${tax}")
print(f"Total: ${total}")