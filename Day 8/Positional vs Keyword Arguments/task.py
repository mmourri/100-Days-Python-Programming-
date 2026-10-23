# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")


# greet_with_name("Jack Bauer")

# Function with more than 1 input

def greet_with_inputs(name, age):
    print(f"Hello {name}?")
    print(f"Are you {age} years old?")

greet_with_inputs("Alice", 30)

def greet_with(name = "Alice", location = "Houston"):
    print(f"Hallo {name}")
    print(f"Welcome to {location}")
