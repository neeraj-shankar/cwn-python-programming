# Coffee Maker Machine
water_available = 300
milk_available = 100
coffee_available = 50
money_available = 2.5

MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18
        },
        'cost': 1.5
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24
        },
        'cost': 2.5
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24
        },
        'cost': 3.0
    }
}

profit = 0
resources = {
    'milk': 200,
    'water': 100,
    'coffee': 100
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Milk: {resources['milk']}ml")
    print(f"Money: ${profit}")


def is_resources_sufficient(order_ingredients):
    """" Returns True when order can be made, False when ingredients insufficient """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_coins():
    """ Returns the total calculated from the coins"""
    print(f"Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, order_cost):
    """ Returns True if payment successful and returns False if insufficient fund added"""
    if money_received >= order_cost:
        global profit
        change = money_received - order_cost
        profit += order_cost
        print(f"Total change {change}")
        return True
    else:
        print("Sorry, that is not enough money. Money Refunded. ")
        return False


def make_coffee(drink_name, order_ingredient):
    """ Deduct the required ingredients from the resources"""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Your coffee is ready")


if __name__ == '__main__':
    is_on = True
    while is_on:
        choice = input(f"What would you like? (espresso/latte/cappuccino): ")
        if choice == 'report':
            print_report()

        elif choice == 'off':
            is_on = False
        else:
            order_choice = MENU[choice]
            order_ingredients = order_choice['ingredients']
            order_cost = order_choice['cost']
            print(order_ingredients)
            print(order_cost)
            if is_resources_sufficient(order_ingredients):
                payment = process_coins()
                if is_transaction_successful(payment, order_cost):
                    make_coffee(order_choice, order_ingredients)
