# Prompt the user for input
month_number = int(input("Please enter the number of the month: "))

# Use match-case to determine the month name
# case {input} if it is 1,2,3 ...
match month_number:
    case 1: month = "January" # if input is 1
    case 2: month = "February" # if input is 2
    case 3: month = "March" # and so on
    case 4: month = "April"
    case 5: month = "May"
    case 6: month = "June"
    case 7: month = "July"
    case 8: month = "August"
    case 9: month = "September"
    case 10: month = "October"
    case 11: month = "November"
    case 12: month = "December"
    case _: month = "Error: Please enter a number between 1 and 12."

# Single output statement
print(f"The name of the month is {month}.")
