import random
from art import *
from game_data import data

# https://www.higherlowergame.com/
# https://appbrewery.github.io/python-day14-demo/

def format_data(account):
    """Return the format account data into printable format."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}."

def check_answer(user_guess, a_followers, b_followers):
    """Return if the user got a right answer after taking user's guess and the follower count."""
    # Use if statement to check if user guess is correct.
    if a_followers > b_followers:
        return user_guess == "a"
    elif a_followers < b_followers:
        return user_guess == "b"

# Display art.
print(logo)

score =0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:
    # Generte a random account from the game data.
    # Make the account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask the user for a guess.
    guess = input(f"Who has more followers? Type A or B: ")

    # Clear the screen
    print("\n" * 20)
    print(logo)

    # Check if user guess is correct.
    # - Get the followers count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # Score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score is: {score}.")
    else:
        print(f"Sorry, That's wrong! Final score is: {score}.")
        game_should_continue = False
