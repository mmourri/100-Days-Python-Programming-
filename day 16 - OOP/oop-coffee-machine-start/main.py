from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

coffee_maker.report()
money_machine.report()

while is_on:
    drinks = menu.get_items()
    option = input("What would you like? (coffee/report): ")
    if option == "report":
        coffee_maker.report()
        money_machine.report()
    elif option == "off":    
        is_on = False
    elif option == "coffee":
        choice = input(f"What's kind of coffee would you like? ({drinks}): ")
        if choice == "off":
            is_on = False
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    else:
        print("Sorry, You have entered the worng option.")
