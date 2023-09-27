from functools import *

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""
print(logo)
def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def calc(prev_ans, operands):
    while True:
        operator = input('Select operator to use (+, -, *, /) or "leave" to exit: ')
        if operator == 'leave':
            break

        x = input('Enter operands: ').split()
        operands = [int(num) if num.isdigit() else float(num) for num in x]

        operands.insert(0,float(prev_ans))

        if operator == '+':
            result = reduce(add, operands)
        elif operator == '-':
            if operands[0]==0:
                result =  reduce(subtract, operands[1:])
            # Reverse subtraction
            else:
                result = reduce(subtract, operands)
        elif operator == '*':
            result = reduce(multiply, operands)
        elif operator == '/':
            result = reduce(divide, operands)
        else:
            print('Invalid input')
            continue

        print(result)
        choice = input("Would you like to continue the operation? y/n: ")
        if choice != 'y':
            break

        prev_ans = result

calc('0', [])