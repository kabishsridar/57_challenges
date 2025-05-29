import random # import random module for answers
def answers(): # define a function named answers to choose answers
    choices_lst =["Yes", "No", "Maybe", "Ask"] # initiate choice lst as the poosible answers list from the question
    choice = [] # initiate an empty list choice
    n = random.randint(1,4) # use random module to select the numbers between 1 to 4
    if n == 1: # each numbers represent each answer
        choice = choices_lst[0]
    elif n == 2:
        choice = choices_lst[1]
    elif n == 3:
        choice = choices_lst[2]
    elif n == 4:
        choice = choices_lst[3]
    print(choice) # display the choice in last of the function
que = input("What's your question? ") # prompt the user for question from user
if __name__ == "__main__":
    answers()