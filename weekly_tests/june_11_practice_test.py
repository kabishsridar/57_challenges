inp = input("address: ") # prompt the user for the address
def defanging(inp): # defining a function to defang
    result = [] # initiating result as an empty list
    for char in inp: # loop through each character in the inp
        if char != ".": # if the character is not a . then append directly
            result.append(char)
        if char == ".": # else, append after adding list brackets
            char = "[.]"
            result.append(char)

    for char in result:
        print(char, end="") # to display the list in format of string for legible
defanging(inp) # calling the function