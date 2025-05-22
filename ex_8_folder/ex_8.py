people = int(input("How many people? ")) # prompt user for number of people
pizza = int(input("How many pizzas do you have? ")) # prompting user for number of pizzas
slices_per_pizza = int(input("Enter number of slices per pizza: ")) # prompting user for slices per pizza

total_slices = pizza * slices_per_pizza # total number of slices will be pizza * slices per pizza

slice_per_person = total_slices // people # it will be the number of slices each person recieves
leftover_slices = total_slices % people # the remainder represent the extra or leftover pieces

print(f"{people} people with {pizza} pizzas") # displaying the datas
print(f"Each person gets {slice_per_person} pieces of pizza.") # displaying the slices for each person
print(f"There are {leftover_slices} leftover pieces.") # displaying the remaining leftover slices