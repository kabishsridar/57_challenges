while True: # loop until it breaks
    rate = input("What is the rate of return? ") # prompt the user for rate
    if rate == "0": # if it is 0 or non digit display error message
        print("Sorry, DivisionByZeroError")
    elif not rate.isdigit():
        print("Sorry, Only integers accepted")
    else: # if it is a digit, convert to integer, and break out of function
        rate = int(rate)
        break

years = 72/rate # calculate years by given formula
print(f"It will take {years} years to double your initial investment") # display the output