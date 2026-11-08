from cmath import pi

from animal import Animal
from fish import Fish

nemo = Fish()

nemo.swim() # Output: Moving in water.
nemo.breathe() # Output: Inhale, Exhale. Fish are breathing through gills.
print(nemo.num_eyes) # Output: 2

names = ["John", "Alice", "Bob"]
ages = [25, 30, 35]

my_dict = dict(zip(names, ages))

print(my_dict)

# Slicing
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys[2:5]) # Output: ['c', 'd', 'e']
print(piano_keys[2:]) # Output: ['c', 'd', 'e', 'f', 'g']
print(piano_keys[2:5:2]) # Output: ['c', 'e']
print(piano_keys[::2]) # Outpyt: ['a', 'c', 'e', 'g']
