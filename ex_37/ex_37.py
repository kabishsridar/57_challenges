import random # importing random module to choose password
min_length = int(input("What's the length of password? ")) # prompting user for length of password
spl_char = int(input("How many special character? ")) # prompting user for number of special character
num = int(input("How many numbers? "))# prompting the user for number of integers

alphabets = list("abcdefghijklmnopqrstuvwxyz") # assigning alphabets, special characters and numbers
special = list("!@#$%^&*`~")
numbers = list("1234567890")
password = []

""" pc_spl = random.randint(1, len(special)-1)
pc_num = random.randint(1, len(numbers)-1)
pc_alphabets = random.randint(1, len(alphabets)-1) """

if spl_char + num > min_length: # the sum of special character and integers should not exceed maximum length
    print("Error. sum of spl character and numbers exceed maximum length.")
else:
    password =[] # initiate password as an empty list and track the password

    for i in range(spl_char):
        password.append(random.choice(special)) # choice helps to choose the random element from the list
    for i in range(num):
        password.append(random.choice(numbers))
    remaining_length = max(min_length - len(password), 0)
    for i in range(remaining_length):
        password.append(random.choice(alphabets))
    
    random.shuffle(password) # it will shuffle the order of password as , first it will give n spl char, num and then alphabet in order, so we are shuffling it
    
    final_password = ''.join(password) # converting list to string
    print(f"Your password is: {final_password}")