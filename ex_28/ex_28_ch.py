total = 0
attempts = 0
n = int(input("enter how many numbers to add: "))
for number in range(n): # loop for 5 numbers
    num = (input("Enter a number: ")) # prompt the number
    if not num.isdigit():
        attempts += 1
        continue
    else:
        num = int(num)
        total += num # adds total 
print(f"The total is {total} and the attempts are {attempts}") # display the total