enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies() # Output: enemies inside function: 2
print(f"enemies outside function: {enemies}") # Output: enemies outside function: 1

# Local scope
def drink_potion():
    potion_solution = 2 # potion_solution is a local variable
    print(potion_solution)

drink_potion() # Output: 2
# print(potion_solution) # Output: NameError: name 'potion_solution' is not defined

# Global scope
player_health = 100 # player_health is a global variable

def game():
    player_health = 90
    print(player_health) 

game() # Output: 90
print(player_health) # Output: 100

def health():
    def drink_potion():
        potion_strength = 2 # potion_strength is a local variable
        print(player_health) # Output: 100

    drink_potion()

print(player_health) # Output: 100
