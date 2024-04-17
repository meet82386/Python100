import coffee_data


def enough_resources(coffee):
    """Functions checks if enough resources are available or not."""
    required = coffee_data.MENU.get(coffee).get("ingredients")

    for item, amount in required.items():
        if coffee_data.resources.get(item) < amount:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def money_count(coffee):
    """Collects money from user and checks if amount is sufficient to make coffee. Also returns change."""
    pennies = float(input("Enter number of pennies: "))
    nickels = float(input("Enter number of nickels: "))
    dimes = float(input("Enter number of dimes: "))
    quarters = float(input("Enter number of quarters: "))

    total_value = (0.01 * pennies) + (0.05 * nickels) + (0.1 * dimes) + (0.25 * quarters)
    required_value = coffee_data.MENU.get(coffee).get("cost")
    difference = total_value - required_value

    if difference < 0:
        print("No enough money to get coffee. ")
        print(f"You have entered {round(required_value - total_value, 2)} less.")
        return False

    if difference > coffee_data.resources.get('money'):
        print("We are running out of change, sorry.")
        return False

    coffee_data.resources['money'] = coffee_data.resources.get('money') + required_value

    if difference != 0:
        print(f"Wait for {coffee} on your table, Here is your ${round(difference, 2)} change")
    return True


def make_coffee(coffee):
    """Makes coffee using available resources"""
    for item, amount in coffee_data.MENU.get(coffee).get("ingredients").items():
        coffee_data.resources[item] = coffee_data.resources.get(item) - amount


while True:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    valid_inputs = ["espresso", "latte", "cappuccino", "off", "report"]

    if coffee_type not in valid_inputs:
        print("Invalid input.")
        continue

    if coffee_type in valid_inputs[:3]:
        if not enough_resources(coffee_type) or not money_count(coffee_type):
            continue
        make_coffee(coffee_type)

    if coffee_type == "off":
        break

    if coffee_type == "report":
        print(f"Water: {coffee_data.resources.get('water')}ml")
        print(f"Milk: {coffee_data.resources.get('milk')}ml")
        print(f"Coffee: {coffee_data.resources.get('coffee')}g")
        print(f"Money: ${coffee_data.resources.get('money')}")
