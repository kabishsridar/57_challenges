import csv
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
def write_csv(purposes, amounts): # storing to csv file
    file = open('expenses.csv', 'w') # opening fule
    writer = csv.writer(file)
    writer.writerow(['Purpose', 'Amount']) # this will be the heading
    for i in range(len(amounts)):
        writer.writerow([purposes[i], amounts[i]]) # store every data one by one