from main import MENU, resources

cost = 0

# quarter = 0.25 dime = 0.10, nickle = 0.05, penny = 0.01
quarter = 0.25
dime = 0.10
nickle = 0.05
penny = 0.01
machine_on = True
# TODO: Check if resources are sufficient
def make_coffee(resources, drink, money, choice):
    resources['water'] -= drink['ingredients']['water']
    
    resources['coffee'] -= drink['ingredients']['coffee']

    resources['money'] += money

    if choice == 'latte' or choice == 'cappuccino':
            resources['milk'] -= drink['ingredients']['milk']
    
    print(f"Here is your {choice} ☕. Enjoy!")

def sufficient(resources, drink, choice):
        if resources['water'] < drink['ingredients']['water']:
            print("Sorry there is not enough water.")
            return 0 
        elif resources['coffee'] < drink['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")
            return 0 
        if choice == 'latte' or choice == 'cappuccino':
            if resources['milk'] < drink['ingredients']['milk']:
                print("Sorry there is not enough milk.")
                return 0 

def process_change(money, cost):
        if money < cost:
            print("Sorry that's not enough money. Money refunded.")
            return 0
        elif money > cost:
            change = money - cost
            print("Here is ${:.2f} dollars in change.".format(change))


# TODO: 1. Print report of all coffee machine resources

def print_report(rsrc):
    print(f"Water: {rsrc['water']}ml")
    print(f"Milk: {rsrc['milk']}ml")
    print(f"Coffee: {rsrc['coffee']}g")
    print(f"Money: ${rsrc['money']}")

# TODO: 2. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        machine_on = False
    elif choice == 'report':
        print_report(resources)
    else:
        drink = MENU[choice]
        cost = MENU[choice]['cost']

        # TODO: 4. Check if resources are sufficient
        if sufficient(resources, drink, choice) == 0: 
            continue

        # TODO: 3. Process coins
        money = int(input("How many quarters?: ")) * quarter
        money += int(input("How many dimes?: ")) * dime
        money += int(input("How many nickles?: ")) * nickle
        money += int(input("How many pennies?: ")) * penny

        if process_change(money, cost) == 0:
            continue

        # TODO: 4. Make Coffee
        make_coffee(resources, drink, money, choice)



