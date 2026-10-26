# There is no Block scope in Python. 

if True:
    a_variable = 10
    print(a_variable) # Output: 10

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) # Output: Skeleton

def create_enemy():
    # initialize a new enemy inside the function
    # new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy) # Output: NameError: name 'new_enemy' is not defined
