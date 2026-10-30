import data

profit = 0
MENU = data.menu
resources = data.resources

# Todo: 1. Print report of all coffee resources.

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pannies? ")) * 0.01
    return total

def is_transaction_success(money_recieved, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here's your ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the ingredients used from the resources."""
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# Todo: 2. Check resources sufficient to make drink order.
is_on = True

while is_on:
    option = input("What would you like? (coffee/report): ")
    if option == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")
    elif option == "off":
        is_on = False
    elif option == "coffee":
        drink_choice = input("What's kind of coffee would you like? (espresso/latte/cappuccino): ")
        if drink_choice == "off":
            is_on = False
        else:
            drink = MENU[drink_choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_success(payment, drink["cost"]):
                    make_coffee(drink_choice, drink["ingredients"] )
    else:
        print("Sorry, You have entered the worng option.")
