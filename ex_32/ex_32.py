import random # import random module to guess the number by the system

def choose_difficulty(level): # define a function named difficulty level
    if level == 1: # set the range according to the question for each levels
        return random.randint(1, 10)
    elif level == 2:
        return random.randint(1, 100)
    elif level == 3:
        return random.randint(1, 1000)
    else:
        return None

def play_game(): # define a function named play_game
    print("Let's play Guess the Number.") # instruct the user that it is a game
    
    while True: # use while loop and ask for difficulty level and proceed with choose_difficulty function for randint and assign it as num_computer
        print("difficulty levels: \n1. 1 to 10\n2. 1 to 100\n3. 1 to 1000")
        difficulty = int(input("Pick a difficulty level (1, 2 or 3): "))
        num_computer = choose_difficulty(difficulty)
        if num_computer is None:
            print("Enter a valid digit between 1 and 3.")
            continue
        break
# initiate guess_count as 0 to track the number of guesses
    guess_count = 0

    while True: # use a while loop and prompt for the number from user and add 1 to guess_count
        guess = input("I have my number. What's your guess? ")
        guess_count += 1 # 

        if not guess.isdigit(): # if the input from the user is not a number, display an error message
            print("Invalid input. Please enter a number.")
            continue

        guess = int(guess)
         
        if guess < num_computer: # if guess in less than num_computer, display Too low
            print("Too low. Guess again:")
        elif guess > num_computer: # if guess is greater tha n num_computer, display Too high
            print("Too high. Guess again:")
        else: # else, display the number of guesses and you got it message and break
            print(f"You got it in {guess_count} guesses!")
            break
 
def loop(): # define a function loop and prompt the user whether to play again
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != 'y': # if y, then loop it
            print("Goodbye!") # else, Goodbye
            break

if __name__ == "__main__":
    loop()