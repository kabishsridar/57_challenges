import random

def choose_difficulty(level):
    if level == 1:
        return random.randint(1, 10)
    elif level == 2:
        return random.randint(1, 100)
    elif level == 3:
        return random.randint(1, 1000)
    else:
        return None

def play_game():
    print("Let's play Guess the Number.")
    
    while True:
        print("difficulty levels: \n1. 1 to 10\n2. 1 to 100\n3. 1 to 1000")
        difficulty = int(input("Pick a difficulty level (1, 2 or 3): "))
        num_computer = choose_difficulty(difficulty)
        if num_computer is None:
            print("Enter a valid digit between 1 and 3.")
            continue
        break

    guess_count = 0

    while True:
        guess = input("I have my number. What's your guess? ")
        guess_count += 1

        if not guess.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        guess = int(guess)
        
        if guess < num_computer:
            print("Too low. Guess again:")
        elif guess > num_computer:
            print("Too high. Guess again:")
        else:
            print(f"You got it in {guess_count} guesses!")
            break

def loop():
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    loop()