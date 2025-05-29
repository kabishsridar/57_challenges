# picking a winner
import random # import the module random to choose the Winner

array = [] # initiate array as an empty list
while True: # untill the input is empty the loop should ask for the name and append it to the array
    name = input("Enter a name:" )
    array.append(name)
    if name =="":
        break

n = len(array) # find number of person in the array
ran = random.randint(1, n) # choose the winner by using random
print(f"the Winner is ...{array[ran]}") # display the winner.