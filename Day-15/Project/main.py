from data import MENU
from data import resources

def moneyHandler():
    # Todo : 3. Check resources sufficient?
    # a. Prompt user to insert coins
    # b. Calculate the monetary value of the coins inserted
    # c. Check that the user has inserted enough money to purchase the drink they selected.
    # d. If they haven’t inserted enough money, the program should display “​Sorry that’s not enough money. Money refunded.​”.
    # e. If the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g. Water: 100ml Milk: 50ml Coffee: 76g Money: $2.5
    # f. If the user has inserted too much money, the machine should offer change.
    # g. The change should be rounded to 2 decimal places.
    # h. Make the user choose the drink again.
    print("Please insert coins")
    quarters=int(input("How many quarters?: "))
    dimes=int(input("How many dimes?: "))
    nickles=int(input("How many nickles?: "))
    pennies=int(input("How many pennies?: "))
    total=0.25*quarters+0.1*dimes+0.05*nickles+0.01*pennies
    return total

totalMoney=0
while(True):
    # Todo :Prompt user by asking “​What would you like? (espresso/latte/cappuccino):​” 
    # a. Check the user’s input to decide what to do next.  
    # b. The prompt should show every time action has completed, e.g. once the drink is 
    # dispensed. The prompt should show again to serve the next customer.
    choice=str(input("Prompt user by asking “​What would you like? (espresso/latte/cappuccino): "))
    if(choice.lower()=="off"):
        print("Machine is shutting down")
        break
    elif(choice.lower()=="report"):
        #Todo : 4. Print report
        print("Water: ",resources["water"])
        print("Milk: ",resources["milk"])
        print("Coffee: ",resources["coffee"])
        print("Money: ",totalMoney)
    elif(choice.lower()=="espresso" or choice.lower()=="latte" or choice.lower()=="cappuccino"):
        amountGiven=moneyHandler()
        if(resources["water"]<MENU[choice]["ingredients"]["water"]):
            print("Sorry there is not enough water")
            continue
        elif(resources["milk"]<MENU[choice]["ingredients"]["milk"]):
            print("Sorry there is not enough milk")
            continue
        elif(resources["coffee"]<MENU[choice]["ingredients"]["coffee"]):
            print("Sorry there is not enough coffee")
            continue
        resources["water"]-=MENU[choice]["ingredients"]["water"]
        resources["milk"]-=MENU[choice]["ingredients"]["milk"]
        resources["coffee"]-=MENU[choice]["ingredients"]["coffee"]
        if(amountGiven<MENU[choice]["cost"]):
            print("Sorry that's not enough money. Money refunded.")
        elif(amountGiven>MENU[choice]["cost"]):
            change=round(amountGiven-MENU[choice]["cost"],2)
            print(f"Here is ${change} in change")
            totalMoney+=MENU[choice]["cost"]
            print(f"Here is your {choice} ☕️. Enjoy!")
        else:
            totalMoney+=MENU[choice]["cost"]
            print(f"Here is your {choice} ☕️. Enjoy!")
