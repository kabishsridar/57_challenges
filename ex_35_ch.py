import random # import random module
array = [] # initiate array as an empty list

def play(): # define a function named play
    while True: # loop untill the user enters empty string
        name = input("Enter a name: ") # prompting for person name
        if name == "":
            break
        array.append(name) # add the name to array

    if array:
        ran = random.randint(0, len(array) - 1)  # choose winner
        winner = array[ran]  # Store the winner before removing
        print(f"The Winner is ... {winner}") # display the winner
        print(winner)

        array.pop(ran)  # Remove the winner from the list
        print(f"Removing {winner} from the array...") # display the list after removing winner
        print("Updated array:", array)

play()

while array:  # Ensure there are players left
    prompt = input("Do you want to play again after removing the contestant (y/n): ")
    if prompt.lower() == "y":
        play()
    else:
        print("Thank you for playing. The game ends.")
        break