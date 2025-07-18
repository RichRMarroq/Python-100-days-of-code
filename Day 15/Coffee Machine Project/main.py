MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

def print_resources():
    """Prints out the keys and values of the Global Dict 'Resources' in a user readable format."""
    for key in resources:
        if key == "water" or key == "milk":
            print(f"{key.title()}: {resources[key]}ml")
        elif key == "coffee":
            print(f"{key.title()}: {resources[key]}g")
        else:
            print(f"{key.title()}: ${resources[key]}")

def check_resources(selection):
    """Takes in the user selection and checks the if Resources is sufficient for required ingredients. Returns 'True' if there is enough resources."""
    for ingredient, resource_value in MENU[selection]["ingredients"].items():
        if resource_value > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def ask_for_coins(selection):
    """Prompts the user to insert coins starting with Quarters down to Pennies. Returns total value of coins inserted."""
    print(f"A {selection.title()} costs ${MENU[selection]['cost']}")
    print("Please insert coins")
    quarter_value = int(input("How many quarters: ")) * .25
    dime_value = int(input("How many dimes: ")) * .10
    nickel_value = int(input("How many nickels: ")) * .05
    penny_value = int(input("How many pennies: ")) * .01
    return quarter_value + dime_value + nickel_value + penny_value

def make_drink(selection, money_inserted):
    """Deduct ingredients from the total resources and print out drink selection made."""
    for key, value in MENU[selection]["ingredients"].items():
        resources[key] -= value
    resources["money"] += MENU[selection]["cost"]
    if money_inserted > MENU[selection]["cost"]:
        change = money_inserted - MENU[selection]["cost"]
        print(f"Here is your change: ${change}")
        print(f"Enjoy your {selection}! ☕")




on = True
while on:
    selection = input("What would you like? (espresso/latte/cappuccino): ")
    if selection.lower() == "off":
        on = False
        continue
    if selection.lower() == "report":
        print_resources()
        continue

    if check_resources(selection):
        #process coins
        money_inserted = ask_for_coins(selection)
        print(f"You have inserted ${money_inserted}")
        #Check if money inserted is enough
        if money_inserted >= MENU[selection]["cost"]:
            make_drink(selection, money_inserted)
        else:
            print(f"Sorry that's not enough money. ${money_inserted} refunded. Please place a new order.")
    
    