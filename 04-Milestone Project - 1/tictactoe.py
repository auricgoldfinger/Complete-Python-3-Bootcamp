import math
from os import system
from sys import platform
from copy import deepcopy
from random import randint

debug = False

def print_debug(s) :
    ''' Prints the given text if debug is enabled '''
    if (debug) : print(s)

clear_output = (lambda: system('cls')) if platform.startswith("win") else (lambda: system('clear'))

def print_help(board):
    ''' Print how you can enter your input '''
    clear_output()
    board_backup = deepcopy(board)
    clear_board(board)
    print("\nTo place your move on the board, enter the number corresponding to the following grid:\n")
    for i in range(0,9):
        place_on_board(board, f"{i+1}",i)
    print_board(board)
    clear_board(board)
    board.clear()
    board.extend(board_backup)
    print_board(board)
    

def print_board(board) :
    '''  Print the current board '''

    for i, row in enumerate(board):
        print(f"\t{row[0]:^3}|{row[1]:^3}|{row[2]:^3}")
        if i < 2 :
            print(f"\t-----------")

    print('')

def calculate_place(place):
    ''' 
    Calculate the place of the given number on the board

    OUTPUT = (row, col)
    '''
    row = int(math.floor(place / 3))
    col = place % 3
    return (row,col)

def place_on_board(board, char,place):
    row, col = calculate_place(place)

    print_debug(f"row: {row}, col: {col}")
    if (board[row][col] == '' or char == ''):
        board[row][col] = char
        return True
    else:
        print("That spot is already taken")
        return False

def check_board(board, place):
    '''
    Check whether there's a win
    
    OUTPUT = True if there's a win based on the current place
    '''
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

def clear_board(board):
    ''' Remove all entries from the board '''

    for i in range(0,9):
        place_on_board(board, '',i)

def check_empty_spot(board):
    '''
    Check if there's still an empty spot on the board

    OUTPUT = True if there are still empty spots left
    '''

    for row in board:
        if '' in row: return True
    else: return False

def read_player_preferences(nrplayers):
    player_list = []
    for i in range(0,nrplayers):
        player_name = input(f"\nPlayer {i+1}, what's your name? ")
        player_marker = input(f"Hi, {player_name}, with which marker will you play? ")

        marker_taken = True
        while marker_taken:
            for otherplayer in player_list:
                if otherplayer['marker'] == player_marker:
                    player_marker = input(f"{otherplayer['name']} is already playing with {otherplayer['marker']}. Choose another one: ")
                    break
            else:
                marker_taken = False

        print(f"Thank you, {player_name}, you'll be playing with {player_marker}")
        player_list.append({'number': i+1, 'name': player_name, 'marker': player_marker})

    return player_list

def read_user_input() :
    ''' Keep reading for user input until the user enters 'q' '''

    clear_output()
    board = [['' for j in range(0,3)] for i in range(0,3)]

    players = read_player_preferences(2)

        player = players[0] if randint(0,1) == 1 else players[1]
        print(f"\n\n\t{player['name']} will start this game.\n\n")

    ask_for_input = True
        while ask_for_input :
            yourinput = input(f"{player['name']}, feed me a number from 1 to 9 ([h]elp, [q]uit): ")
            if yourinput == 'q':
            print("Thank you for playing!")
            exit()
            elif yourinput == 'h':
                print_help(board)
                continue
            elif (not yourinput.isdigit()) :
                print("Oh come on.")
                continue

            place = int(yourinput)-1

            if place > 8 or place < 0:
                print("Number out of range.")
                continue

            if place_on_board(board, player['marker'], place):
                clear_output()
                title = "Current board\n"
                for c in title:
                    title += "="
                
                print(f"\n{title}\n")
                print_board(board)
                if check_board(board, place):
                    print(f"We have a winner! {player['name']} wins this round!")
                return
                elif check_empty_spot(board):
                    player = players[1] if player == players[0] else players[0] 
                else:
                    print("It's a tie!")
                return

read_user_input()
print("")