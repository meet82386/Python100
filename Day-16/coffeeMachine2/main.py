import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
machine = MoneyMachine()


while True:
    user_input = input(f"Enter coffee name: ({menu.get_items()}) ")

    if user_input == "off":
        break
    elif user_input == "report":
        coffee_maker.report()
        machine.report()
    else:
        item = menu.find_drink(user_input)
        if item is not None:
            if machine.make_payment(item.cost) and coffee_maker.is_resource_sufficient(item):
                coffee_maker.make_coffee(item)
