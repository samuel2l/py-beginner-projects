from random import *
from replit import clear
computer_number=randint(1,100)
print("I am thinking of a number between one and 100")

def guess_game():
    difficulty=input('what difficuly? hard or easy ').lower()
    if difficulty=='hard':
        attempts=5
        attempts=int(attempts)
    elif difficulty=='easy':
        attempts=10

    while attempts>0:
        print(f"You have {attempts} attempts left. ")
        x=int(input('Enter a guess '))
        if x==computer_number:
            print('You got it wow')

            break
        else:
            if x > computer_number:
                print('Oof too high')
            elif x<computer_number:
                print('oof too low')
            else:
                continue
            attempts-=1
            if attempts==0:
                print("You are out of guesses. ")
                play_again= input("want to play again? y/n ").lower()
                if play_again=='y':
                    clear()
                    guess_game()
                else:
                    break
guess_game()