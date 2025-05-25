def multiply_table(n): # defining a function named multiply_table
    for i in range(n + 1): # loop for maximum number entered by user (n + 1 is used as for loop starts from 0)
        for j in range(n + 1):
            print(f"{i} X {j} = {i * j}") # displaying the output
if __name__ == "__main__":
    n = int(input("Enter maximum number of multiplication table(from 2 to 200): "))
    multiply_table(n)