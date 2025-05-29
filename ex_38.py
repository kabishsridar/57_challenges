prompt = input("Enter a list of numbers, seperated by spaces: ").split()

def filterEvenNumbers(prompt):
    even = []
    for number in prompt:
        number = int(number)
        if number % 2 == 0:
            even.append(number)
        else:
            pass
    print(f"The even numbers are {even}")
filterEvenNumbers(prompt)