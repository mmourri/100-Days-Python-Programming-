# Modifying Global Scope

enemies = 1

# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}") # Output: enemies inside function: 2

# increase_enemies()
# print(f"enemies outside function: {enemies}") # Output: enemies outside function: 2

def increase_enemies(enemy):
    return enemy + 1
    
enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}") # Output: enemies outside function: 2
