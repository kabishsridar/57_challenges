dict =  {
     "products" : [
 {"name": "Widget", "price": 25.00, "quantity": 5 },
 {"name": "Thing", "price": 15.00, "quantity": 5 },
 {"name": "Doodad", "price": 5.00, "quantity": 10 }
    ]
}

while True:
    pname = input("What is the product name? ").strip()
    found = False
    
    for product in dict["products"]:
        if product["name"].lower() == pname.lower():
            print(f"Product: {product['name']}")
            print(f"Price: ${product['price']}")
            print(f"Quantity: {product['quantity']}")
            found = True
            break
    
    if found:
        break 
    
    print("Sorry, that product was not found in our inventory.")
