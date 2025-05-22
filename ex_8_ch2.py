import math # importing math module to round off the value
people = input("How many people? ") # prompting the user for number of people
slices_per_person = input("Enter number of pieces each person wants: ") # prompting for slices each person wants
slices_per_pizza = input("Enter number of slices per pizza: ") # prompting for slices per pizza

# Function to check whether the input is a positive integer
def isinteger(a):
    return a.isdigit() and int(a) > 0

if isinteger(people) and isinteger(slices_per_person) and isinteger(slices_per_pizza): # according to the conditions, it shoud be a positive integer
    people = int(people) # converting to integer
    slices_per_person = int(slices_per_person) # converting to integer
    slices_per_pizza = int(slices_per_pizza) # converting to integer

    total_slices_needed = people * slices_per_person # this will be the slices needed for all people
    pizzas_needed = math.ceil(total_slices_needed / slices_per_pizza) # returns the smallest number more than the total_slices_needed / slices_per_pizza

    print(f"{people} people want {slices_per_person} slice(s) each.") # displays how many slices we need
    print(f"You need to buy {pizzas_needed} pizza(s).") # displays how many pizzas we need
else:
    print("Please enter valid positive numeric values.")
