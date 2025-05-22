people = input("How many people? ")  # prompt user for number of people
pizza = input("How many pizzas do you have? ")  # prompting user for number of pizzas
slices_per_pizza = input("Enter number of slices per pizza: ")  # prompting user for slices per pizza

plural = ""  # variable to store pluralized word

# function to check whether the input is an integer
def isinteger(a):
    if a.isdigit():
        return True
    else:
        return False

# pluralisation function to decide singular/plural form for slices per person
def pluralisation():
    global plural
    if slice_per_person == 1:
        plural = "piece"
    else:
        plural = "pieces"

    people = int(people)  # convert input to integer
    pizza = int(pizza)  # convert input to integer
    slices_per_pizza = int(slices_per_pizza)  # convert input to integer

# checking that all inputs are integers before performing operations
if isinteger(people) and isinteger(pizza) and isinteger(slices_per_pizza):
    total_slices = pizza * slices_per_pizza  # total number of slices will be pizza * slices per pizza
    slice_per_person = total_slices // people  # it will be the number of slices each person receives
    leftover_slices = total_slices % people  # the remainder represents the extra or leftover pieces

    pluralisation()  # call pluralisation to set the correct word for per person

    # plural for leftover (handled separately)
    leftover_plural = "piece" if leftover_slices == 1 else "pieces"

    print(f"{people} people with {pizza} pizzas")  # displaying the data
    print(f"Each person gets {slice_per_person} {plural} of pizza.")  # displaying the slices for each person
    print(f"There are {leftover_slices} leftover {leftover_plural}.")  # displaying the remaining leftover slices
else:
    print("Please enter valid numeric values.")  # error message if input is invalid