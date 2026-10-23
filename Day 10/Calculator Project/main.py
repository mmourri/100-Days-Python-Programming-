from art import logo

print(logo)

# Todo: Write out the different calculator functions.
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Todo: Create a dictionary to map the operator symbols to their corresponding functions.
operation_dictionary = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

# Todo: Use the dictionary to performe the calculation based on the user's input.

def calculator():
    continue_calculation = True
    first_number = float(input("What's the first number?: "))

    while continue_calculation:
        
        for symbol in operation_dictionary:
            print(symbol)
        operation = input("Pick an operation: ")
        second_number = float(input("What's the second number?: "))
    
        calculation_function = operation_dictionary[operation]
        answer = calculation_function(first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {answer}")

        choice = input("Type 'y' to continue calculating with {answer}, ot type 'n' to start new calculation: ")
        if choice == "y":
            first_number = answer
        elif choice == "n":
            continue_calculation = False
            print("\n" * 20)
            print("Starting new calculation...")
            calculator()

calculator()
