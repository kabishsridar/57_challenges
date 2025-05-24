username = input("Enter the username: ") # prompt the user for username
passwd = input("What is your password?  ")

# initiating username and password which is alreay set
user1 = "kabish"
password1 = "abc$123"
user2 = "kamal"
password2 = "123kamal"


def check_password(): # defining a function to check password
    global passwd
    if username == "kabish": # if user name is kabish and password is correct, then print Welcome!
        if passwd == password1:
            print("Welcome!")
        else: # if password is wrong
            print("I don't know you")
    elif username == "kamal": # if password matches
        if passwd == password2: 
            print("Welcome!") 
        else: # if password is wrong
            print("I don't know you")
check_password() # calling function to begin