#doc: https://docs.google.com/document/d/e/2PACX-1vTragRHILyj76AvVgpWeOlEaLBXoxPM_43SdEyffIKtOgarj42SoSAsK6LwLAdHQs2qFLGthRZds6ok/pub
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# drink = MenuItem
# print(drink)
'''
# Menu Class
    - get_items()
    - find_drink(order_name)
'''
# menu = Menu()
# print(menu.get_items())
# latte = menu.find_drink('latte')
# print(latte.ingredients)

'''
# CoffeeMaker Class
    - report()
    - make_coffee(order)
    - is_resource_sufficient(drink)
'''
# coffee_machine = CoffeeMaker()
# print(coffee_machine)
# coffee_machine.report()
# coffee_machine.make_coffee(latte)
# coffee_machine.is_resource_sufficient(latte)

'''
# MoneyMachine Class
    - report()
    - make_payment(cost)
'''
# money = MoneyMachine()
# money.make_payment(latte.cost)
# money.report()
# print(money)

def coffee_machine():
    print('Welcome to coffee machine ☕')
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    options = menu.get_items()
    user_input = input(f'What would you like? ({options}): ')

    if user_input == 'report':
        coffee_maker.report()
        money_machine.report()
        return coffee_machine()
    elif user_input == 'off':
        print('Bye than')
        return
    else:
        drink = menu.find_drink(user_input)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)

    another_coffee = input('Would you like to have another coffee? "yes" or "no": ')
    if another_coffee == 'yes':
        return coffee_machine()

coffee_machine()