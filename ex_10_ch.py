def isinteger(a): # defining a function to check whether it is a digit
    return a.isdigit()
n = int(input("Enter number of items: ")) # prompt user for number of items
subtotal = 0  # initiating subtotal as 0
for loop in range(n): # loop through each items
    price = (input(f"Enter the price of item {loop + 1}: ")) # prompt user for price of item
    quantity = (input(f"Enter the quantity of item {loop + 1}: ")) # prompt usre for number of items
    if isinteger(price) and isinteger(quantity): # checking whether it is a digit
        price = int(price) # convert them to integer
        quantity = int(quantity)        
        item_total = price * quantity # item_total will be the complete price of item
        subtotal += item_total # subtotal will be the total for all items
    if loop == n -1: # executes only after getting last item datas
        tax = subtotal * 0.055 # tax rate mentioned 5.5% so multiplied by 0.55 to get tax
        total = tax + subtotal # grand total
print(f"SubTotal: ${subtotal}") # displaying output
print(f"Tax: ${tax}") 
print(f"Total: ${total}")