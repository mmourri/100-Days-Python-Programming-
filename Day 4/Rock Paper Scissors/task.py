import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

items = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if 0 <= user_choice <= 2:
    print(items[user_choice])

print("Computer chose:\n")
computer_choice = random.randint(0,2)
print(items[computer_choice])

if user_choice > 2 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice == user_choice:
    print("It's a draw!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice < user_choice:
    print("You win!")
