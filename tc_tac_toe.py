board = [' null', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def print_board():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))


def check_winner(var, player):
    if board[1] == var and board[5] == var and board[9] == var:
        print(f'{player} wins. Oof you won on the right diagonal')

    elif board[1] == var and board[2] == var and board[3] == var:
        print(f'{player} wins. Oof you won on the first row, user 2 how did you miss that?')
    elif board[1] == var and board[4] == var and board[7] == var:
        print(f'{player} wins. Oof you won on the first column')
    elif board[3] == var and board[6] == var and board[9] == var:
        print(f'{player} wins. Oof you won on the last column')
    elif board[4] == var and board[5] == var and board[6] == var:
        print(f'{player} wins. Oof you won on the second column')
    elif board[7] == var and board[8] == var and board[9] == var:
        print(f'{player} wins. Oof you won on the last row')
    elif board[2] == var and board[5] == var and board[8] == var:
        print(f'{player} wins. Oof you won on the second column')
    else:
        return False


def game():
    while True:
        if ' ' not in board:
            print("draw")
            break

        while True:
            try:

                player1 = int(input('(X)What position do you want to make your play at? '))
            except ValueError:
                print("Enter a valid position ranging from 1 to 9")
            else:

                if board[player1] == ' ':
                    board[player1] = 'x'
                    print_board()

                    break
                else:

                    if board[player1] == 'x':
                        print('You have already marked that position')
                    else:
                        print('Your opponent has already marked that position, try again')
        if check_winner('x', 'Player 1(X)') is not False or check_winner('o', 'Player 2(O)') is not False:
            break
        while True:
            if ' ' not in board:
                print("draw")
                break
            try:

                player2 = int(input('(O)What position do you want to make your play at? '))
            except ValueError:
                print("Enter a valid position ranging from 1 to 9")
            else:
                if board[player2] == ' ':
                    board[player2] = 'o'
                    print_board()
                    check_winner('o', 'Player 2(O)')
                    if check_winner('o', 'Player 2(O)'):
                        playing = False

                    break
                else:

                    if board[player2] == 'o':
                        print('You have already marked that position')
                    else:
                        print('Your opponent has already marked that position, try again')
        if check_winner('x', 'Player 1(X)') is not False or check_winner('o', 'Player 2(O)') is not False:
            break

game()