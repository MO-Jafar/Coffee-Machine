from file_menu import MENU

current_resource = {"water": 300, "milk": 200, "coffee": 100, "money": 0}


def check_resource(choice):
    """Returns True if ingredients are sufficient, otherwise False."""
    for item in choice:
        if choice[item] > current_resource[item]:
            print(f"Sorry not enough {item}")
            return False
    return True


def check_transaction(payment, cost_of_drink):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if payment >= cost_of_drink:
        change = payment - cost_of_drink
        print(f"Here is your ${change} in change.")
        current_resource["money"] += cost_of_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def calculate_total_coins():
    "Returns total calculated"
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    tot_dollar = float("{:.2f}".format(quarters + dimes + nickles + pennies))
    return tot_dollar


def make_coffee(choice, selected_drink):
    """Deduct the required ingredients from the resources."""
    for item in selected_drink:
        current_resource[item] -= selected_drink[item]
    print(f"Here is your {choice} ☕️ Enjoy!")


is_on = True
while is_on:
    choice = input("What would you like?(espresso/latte/cappuccino):").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water :{current_resource['water']} ml")
        print(f"Milk :{current_resource['milk']} ml")
        print(f"Coffee :{current_resource['coffee']} g")
        print(f"Money :$ {current_resource['money']}")
    else:
        selected_drink = MENU[choice]
        if check_resource(selected_drink["ingredients"]):
            exchanged_money = calculate_total_coins()
            if check_transaction(exchanged_money, selected_drink["cost"]):
                make_coffee(choice, selected_drink["ingredients"])
