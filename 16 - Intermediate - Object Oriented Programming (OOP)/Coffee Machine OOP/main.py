import os
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True
os.system('cls')
my_money_machine = MoneyMachine()
my_coffe_maker = CoffeeMaker()
my_menu = Menu()

my_money_machine.report()


while is_on:
    options = my_menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        my_coffe_maker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(choice)
        if my_coffe_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffe_maker.make_coffee(drink)
