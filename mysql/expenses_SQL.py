import mysql.connector as sqltor
mycon = sqltor.connect(host='localhost', user='root', passwd='2007kabish', database='kabish')
if mycon.is_connected():
    print("Connected to the database")
else:
    print("Failed to connect to the database")
cur = mycon.cursor()
def add_expense(purpose, amount): # function to add expenses
    purposes.append(purpose)
    amounts.append(amount)
def show_total(amounts): # function to display all datas
    total = sum(amounts) # returns sum
    print(f"Total Expense: {total}")
def show_average(amounts): # function to display average
    if amounts != []:
        average = sum(amounts) / len(amounts) # returns average
        print(f"Average Expense: {average}")
    else:
        print("No expenses recorded.")
def show_highest_expense(purposes, amounts): # function to show highest expense
    if amounts != []:
        max_index = amounts.index(max(amounts)) # returns the maximum number in amounts
        print(f"Highest Expense: {purposes[max_index]} - {amounts[max_index]}")
    else:
        print("No expenses recorded.")
def display_all_expense(purposes, amounts):
    if purposes and amounts:
        print("Expenses:")
        for i in range(len(purposes)): # display all datas one by one
            print(f"{i + 1}. {purposes[i]} - {amounts[i]}") 
    else:
        print("No expenses recorded.")
def add_item(purpose, amount): # function to add items
    cur.execute("CREATE TABLE IF NOT EXISTS expenses (PURPOSE VARCHAR(100), AMOUNT FLOAT)")
    cur.execute("INSERT INTO expenses VALUES (%s, %s)", (purpose, amount))
    mycon.commit()
if __name__ == "__main__": # this should run at the beginning
    purposes = [] # initiating purposes and amounts as empty lists
    amounts = []
    while True:
        print("\nenter the number accordingly")
        print("""1. Add Expense
        2. Show total
        3. Show Average
        4. Show highest Expense
        5. Display All Expense
        6. Exit
        """) # instruct the user about the function
        choice = int(input("Enter your choice: ")) # prompt for the choice
        if choice == 1: # calling the functions according to the input
            purpose = input("Enter the purpose: ") # prompt these only when the user needs to add expense
            amount = float(input("Enter the amount: "))
            add_expense(purpose, amount)
            add_item(purpose, amount)
        elif choice == 2:
            show_total(amounts)
        elif choice == 3:
            show_average(amounts)
        elif choice == 4:
            show_highest_expense(purposes, amounts)
        elif choice == 5:
            display_all_expense(purposes, amounts)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")
mycon.close()