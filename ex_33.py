import random
def answers():
    choices_lst =["Yes", "No", "Maybe", "Ask"]
    choice = []
    n = random.randint(1,4)
    if n == 1:
        choice = choices_lst[0]
    elif n == 2:
        choice = choices_lst[1]
    elif n == 3:
        choice = choices_lst[2]
    elif n == 4:
        choice = choices_lst[3]
    print(choice)
que = input("What's you question? ")
if __name__ == "__main__":
    answers()