from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
options=menu.get_items()
while(True):
    choice=str(input(f"​What would you like? {options}: "))
    os.system("cls")
    if(choice.lower()=="off"):
        print("Machine is shutting down")
        break
    elif(choice.lower()=="report"):
        coffee_maker.report()
        money_machine.report()
    elif(choice.lower()=="espresso" or choice.lower()=="latte" or choice.lower()=="cappuccino"):
        drinkDetails=menu.find_drink(choice)
        if(coffee_maker.is_resource_sufficient(drinkDetails) and money_machine.make_payment(drinkDetails.cost)):
            coffee_maker.make_coffee(drinkDetails)
        else:
            continue
    else:
        print("Wrong Input")

