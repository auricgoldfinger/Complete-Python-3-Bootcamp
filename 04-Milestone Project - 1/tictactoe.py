import math
from copy import deepcopy

board = [['' for j in range(0,3)] for i in range(0,3)]
debug = False
player = 'X'

def print_debug(s) :
    if (debug) : print(s)

def print_help():
    global board
    board_backup = deepcopy(board)
    clear_board()
    print("\n\tTo place your move on the board, enter the number corresponding to the following grid:\n")
    for i in range(0,9):
        place_on_board(f"{i+1}",i)
    print_board()
    clear_board()
    board = deepcopy(board_backup)
    print_board()
    

def print_board() :
    global board

    for i, row in enumerate(board):
        print(f"\t{row[0]:^3}|{row[1]:^3}|{row[2]:^3}")
        if i < 2 :
            print(f"\t-----------")

    print('')

def calculate_place(place):
    row = int(math.floor(place / 3))
    col = place % 3
    return (row,col)

def place_on_board(char,place):
    global board
    row, col = calculate_place(place)

    print_debug(f"row: {row}, col: {col}")
    if (board[row][col] == '' or char == ''):
        board[row][col] = char
        return True
    else:
        print("That spot is already taken")
        return False

def check_board(place):
    '''Check whether there's a win'''
    global board
    row, col = calculate_place(place)
    
    # check column
    print_debug(f"{board[0][col]} == {board[1][col]} == {board[2][col]}?")
    if (board[0][col] == board[1][col] == board[2][col]): return True

    # check row
    print_debug(f"{board[row][0]} == {board[row][1]} == {board[row][2]}?")
    if (board[row][0] == board[row][1] == board[row][2]): return True

    # check diagonal

    # check anti-diagonal
    
    return False

def clear_board():
    global board
    for i in range(0,9):
        place_on_board('',i)

def read_user_input() :
    global board, player
    ask_for_input = True
    while ask_for_input :
        yourinput = input(f"Player {player}, feed me a number from 1 to 9: ")
        if yourinput == 'q':
            print("Thank you for playing!")
            exit()
        elif yourinput == 'h':
            print_help()
            continue
        elif (not yourinput.isdigit()) :
            print("Oh come on.")
            continue

        place = int(yourinput)-1

        if place > 8 or place < 0:
            print("Number out of range.")
            continue

        if place_on_board(player, place):
            title = "Current board\n"
            for c in title:
                title += "="
            
            print(f"\n{title}\n")
            print_board()
            if check_board(place):
                print(f"We have a winner! Player {player} wins this round!")
                return

            player = 'O' if player == 'X' else 'X'

read_user_input()