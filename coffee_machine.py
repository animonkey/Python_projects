MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resource(ingredients):
    for x in ingredients:
        if ingredients[x] > resources[x]:
            print(f"Sorry there is not enough {x}")
            return False
    return True
def process_money():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction(received, cost):
    if received >= cost:
        change = round(received - cost,2)
        print(f"Here is ${change}.")
        global money
        money += cost
        return True
    else:
        print("Sorry that's not enought money. Money refunded")
        return False

def make_coffee(drink_name, ingredients):
    for x in ingredients:
        resources[x] -= ingredients[x]
    print(f"Here is your {drink_name}☕️")

money = 0
on = True
while on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[choice]
        if check_resource(drink["ingredients"]):
            payment = process_money()
            if transaction(cost=drink["cost"],received=payment):
                make_coffee(drink_name=choice,ingredients=drink["ingredients"])

        
            

        
