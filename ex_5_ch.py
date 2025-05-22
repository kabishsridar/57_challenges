def isinteger_positive(num_str1,num_str2):
    if num_str1.isdigit() and num_str2.isdigit(): # checks for both whether it is an integer as well as it is a positive integer
        return True
    else:
        print("Only integers allowed.") # else it should return the error message
        return False

def operations(first_num, second_num): # it will perform all arithmetic functions to add, subtract, multiply and divide
    print(f"{first_num} + {second_num} = {first_num + second_num}")
    print(f"{first_num} - {second_num} = {first_num - second_num}")
    print(f"{first_num} * {second_num} = {first_num * second_num}")
    if second_num != 0: # DivisionByZeroError
        print(f"{first_num} / {second_num} = {first_num / second_num}")
    else:
        print("Division by zero is not allowed.")

num1 = input("Enter first number: ") # prompting the user for first number
num2 = input("Enter second number: ") # prompting the user for second number

# Check if inputs are valid integer strings

if isinteger_positive(num1,num2):
    # If both are valid integer strings, convert them
    first_number = int(num1)
    second_number = int(num2)
    operations(first_number, second_number) # calling the function to perform operations
else:
    pass