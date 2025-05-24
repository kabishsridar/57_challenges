print("Enter C to convert from Farenheit to Celsius.") 
print("Enter F to convert form Celsius to Farenheit.")
choice = input("Your choice: ") # prompting for choice

if choice.lower() == "c": # converting to lowercase and check for choice 
    f = int(input("Please enter the temperature in Fahrenheit: ")) # prompt for farenheit
    c = (f - 32) * 5/9 # calculate celsius
    print(f"The temperature in celsius: {c}") # display output
elif choice.lower() == "f": # if it is f
    c = int(input("Please enter the temperature in Celsius: "))
    f = (c * 9/5) + 32 # calculae f
    print(f"The temperature in Farenheir: {f}")
else:
    print("Enter valid input between c and f")
