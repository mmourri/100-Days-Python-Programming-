import random
import my_module

# Generate random integer
random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.my_favorite_number)

# Generate random floating number
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

print("===================")

random_number = random.randint(0, 1)
if random_number == 0:
    print("Heads")
else:
    print("Tails")
