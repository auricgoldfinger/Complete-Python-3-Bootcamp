import math
from os import system
from sys import platform
from copy import deepcopy

board = [['' for j in range(0,3)] for i in range(0,3)]
debug = False
player = 'X'

def print_debug(s) :
    if (debug) : print(s)

clear_output = (lambda: system('cls')) if platform.startswith("win") else (lambda: system('clear'))

def print_help():
    clear_output()
    global board
    board_backup = deepcopy(board)
    clear_board()
    print("\nTo place your move on the board, enter the number corresponding to the following grid:\n")
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
    print_debug(f"Check column {col+1}: {board[0][col]} == {board[1][col]} == {board[2][col]}?")
    if (board[0][col] == board[1][col] == board[2][col]): return True

    # check row
    print_debug(f"Check row    {row+1} : {board[row][0]} == {board[row][1]} == {board[row][2]}?")
    if (board[row][0] == board[row][1] == board[row][2]): return True

    # check diagonal
    if (row == col):
        print_debug(f"Check diagonal")
        if (board[0][0] == board[1][1] == board[2][2]): return True

    # check anti-diagonal
    if (row + col == 3-1):
        print_debug(f"Check anti-diagonal")
        if (board[0][2] == board[1][1] == board[2][0]): return True

    
    return False

def clear_board():
    global board
    for i in range(0,9):
        place_on_board('',i)

def check_empty_spot():
    global board
    for row in board:
        if '' in row: return True
    else: return False

def read_user_input() :
    global board, player
    ask_for_input = True
    while ask_for_input :
        yourinput = input(f"Player {player}, feed me a number from 1 to 9 ([h]elp, [q]uit): ")
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
            clear_output()
            title = "Current board\n"
            for c in title:
                title += "="
            
            print(f"\n{title}\n")
            print_board()
            if check_board(place):
                print(f"We have a winner! Player {player} wins this round!")
                return
            elif check_empty_spot():
                player = 'O' if player == 'X' else 'X'
            else:
                print("It's a tie!")
                return

read_user_input()
print("")