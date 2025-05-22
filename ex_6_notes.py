from datetime import datetime # importing datetime module to get current year
current_year = datetime.now().year # this line gets only the year except time, month, date
current_age = int(input("What is your current age? ")) # prompting user for current age
retirement_age = int(input("At what age would you like to retire? ")) # prompting user for retirement age
print(f"You have {retirement_age - current_age} years left until you can retire.") # displaying the number of years the user have until retirement
print(f"It's {current_year}, so you can retire in {current_year + retirement_age - current_age}") # displaying the year in which the user can retire