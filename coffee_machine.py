from coffee_machine_data import *
from replit import clear
from time import *
def track_resources(coffee):

    for key,value in resources.items():
        resources[key]-= MENU[coffee]["ingredients"][key]
    print(f"Now we only have : {resources} left")

def check_resources(coffee):
    # if   resources["water"] > MENU[coffee]["ingredients"]["water"] and
    for key,value in resources.items():
        if resources[key]>MENU[coffee]["ingredients"][key]:
            return True
def report():
    for key, value in resources.items():
        if key == "water" or key == "milk":
            print(f'{key}: {value}ml')
        else:
            print(f'{key}: {value}g')


def payment():
    coffee_type = input('what would you like to have? ')

    if check_resources(coffee_type):
        quarters= int(input('How many quarters '))
        nickels = int(input('How many nickels '))
        dimes = int(input('How many dimes '))
        pennies = int(input('How many pennies '))
        total= (quarters*0.25)+ (quarters*0.25)+(quarters*0.25)+(quarters*0.25)
        if total<MENU[coffee_type]["cost"]:

            print(f"the {coffee_type} costs {MENU[coffee_type]['cost']}$ but you only gave {total}.")
            remaining_amnt=MENU[coffee_type]["cost"] - total
            print(f"you need {remaining_amnt}$ more ")

        elif total == MENU[coffee_type]["cost"]:
            print("just the right amount")
            track_resources(coffee_type)
        else:
            change=total-MENU[coffee_type]["cost"]
            print(f"Your change is {change}$")
            track_resources(coffee_type)
    else:
        print("We do not have enough resources to grant your request sorry")

    sleep(5)
    print("Some coffee? ")
    clear()
    report()
    payment()



report()
payment()

#if coffee=='expresso':
