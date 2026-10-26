from art import logo
import random

HIGH_LEVEL_TURNS = 5
EASY_LEVEL_TURNS = 10

# Function to check user's guess against actual answer
def check_user_guess(user_guess, actual_guess, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_guess:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_guess:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it! The answer was {actual_guess}.")
        return turns

def set_difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower() 
    if level == "hard":
        return HIGH_LEVEL_TURNS
    else: 
        return EASY_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    choosen_number = random.randint(1, 100)
    print(f"The correct answer is {choosen_number}") # TODO: Remove after testing

    turns = set_difficulty()

    guess = 0

    while guess != choosen_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))        
        turns = check_user_guess(guess, choosen_number, turns)
        if turns == 0:
            print(f"You've run out of guesses, you lose. The correct answer was {choosen_number}.")
            return
        elif guess != choosen_number:
            print("Guess again.")

game()
