import mysql.connector as sqltor
mycon = sqltor.connect(host='localhost', user='root', passwd='2007kabish', database='kabish')
if mycon.is_connected():
    print("Connected to the database")
else:
    print("Failed to connect to the database")
cur = mycon.cursor()
def add_item():
    cur.execute("CREATE TABLE IF NOT EXISTS items (item_id INT AUTO_INCREMENT PRIMARY KEY, item_name VARCHAR(255), price FLOAT, quantity INT)")
    item_name = input("Enter the item name: ")
    price = input("Enter the price: ")
    quantity = input("Enter the quantity of item: ")
    cur.execute("INSERT INTO items (item_name, price, quantity) VALUES (%s, %s, %s)", (item_name, price, quantity))
    mycon.commit()
add_item()
mycon.close()