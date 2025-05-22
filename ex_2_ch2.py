data = input("What is the input string? ") # get the input from the user for the input string  to count the number of characters and store it as data
count = len(data) # store the length of data as count
if data == "" or " ": # if the string is empty, it should return: The user must enter something to the programme
    print("The user must enter something to the programme")
else: # otherwise it should return the output
    print(f"{data} has {count} character")