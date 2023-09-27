#NOT FULLY COMPLETE
from random import *
from replit import clear
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards=[]
dealer_cards=[]
def get_card(player):

    x= int(choice(cards))
    player.append(x)

def get_score(player):


    summ=sum(player)
    return summ

def play():
    while True:
        start_game = input("Play? y or n")
        if start_game == 'y':
            clear()
            print(logo)
            get_card(dealer_cards)
            get_card(dealer_cards)
            get_card(user_cards)
            get_card(user_cards)
            print(user_cards)
            tot= get_score(user_cards)
            print(f" this is tot {tot}")
            tot2= get_score(dealer_cards)
            print(f"your first cards: {user_cards} and your score is {tot}")
            print(f"The dealer's first card: {dealer_cards[0]} ")
            if tot > 21 and tot2 < 21:
                print("user got over 21 you lose")
            elif tot == 21 and tot2 < 21:
                print("user hit blackjack")
            elif tot2 == 21 and tot < 21:
                print("dealer hit blackjack")

            elif tot < 16 and tot2 < 16:
                print(" you have below 16 you need to draw a card")

                get_card(user_cards)
                get_card(dealer_cards)
                less_16_user = get_score(user_cards)
                less_16_dealer = get_score(dealer_cards)
                print(f"your first cards: {user_cards} and your score is {less_16_user}")
                print(f"The dealer's cards: {dealer_cards}, currect score: {less_16_dealer} ")
                if less_16_user > 21 and less_16_dealer < 21:
                    print("user got over 21 you lose")
                elif less_16_user == 21 and less_16_dealer < 21:
                    print("user hit blackjack")
                elif less_16_dealer == 21 and less_16_user < 21:
                    print("dealer hit blackjack")
                elif less_16_dealer==less_16_user:
                    print("Oof a draw")
                elif less_16_user>less_16_dealer:
                    print("user wins")
                elif less_16_dealer>less_16_user:
                    print("dealer wins")
            elif tot2 > tot and tot2 > 16 and tot > 16:
                while tot<21 and tot2<21:
                    again = input('Do you want to draw another card? y or n ')
                    if again=='y':
                        get_card(user_cards)
                        tot = get_score(user_cards)
                        tot2 = get_score(dealer_cards)
                    else:
                        break
                print(f"your first cards: {user_cards} and your score is {tot}")
                print(f"The dealer's cards: {dealer_cards}, currect score: {tot2} ")
                if tot>tot2:
                    print("user wins")
                else:
                    print("dealer wins")


                print("dealer wins")
            elif tot > tot2 and tot2 > 16 and tot > 16:
                print("user wins")
            elif tot == tot2:
                print("oof a draw")

                if tot>21 and tot2<21:
                    print("user got over 21 you lose")

                elif tot==21 and tot2<21:
                    print("user hit blackjack")
                elif tot2==21 and tot<21:
                    print("dealer hit blackjack")

                elif tot<16 and tot2<16:
                    print("  you have below 16 you need to draw a card")
                    if tot<16:
                        get_card(user_cards)
                        print(user_cards)
                        get_card(dealer_cards)
                        less_16_user = get_score(user_cards)
                        print(less_16_user)
                        less_16_dealer = get_score(dealer_cards)
                        print(f"your first cards: {user_cards} and your score is {tot}")
                        print(f"The dealer's cards: {dealer_cards}, currect score: {tot2} ")
                        if less_16_user > 21 and less_16_dealer < 21:
                            print("user got over 21 you lose")
                        elif less_16_user == 21 and less_16_dealer < 21:
                            print("user hit blackjack")
                        elif less_16_dealer == 21 and less_16_user < 21:
                            print("dealer hit blackjack")
                elif tot2>tot and tot2>16 and tot>16:
                    print("dealer wins")
                elif tot>tot2 and tot2>16 and tot>16:
                    print("user wins")
                elif tot==tot2:
                    print("oof a draw")
        else:
            print("okay no game")
            break
play()