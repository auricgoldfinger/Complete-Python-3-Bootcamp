import math

board = [['' for j in range(0,3)] for i in range(0,3)]
debug = True

def print_debug(s) :
    if (debug) : print(s)

def print_help():
    print("\n\tTo place your move on the board, enter the number corresponding to the following grid:")
    for i in range(0,9):
        place_on_board(f"{i+1}",i)
    print_board()
    

def print_board() :
    global board
    title = "Current board\n"
    for c in title:
        title += "="
    
    print(f"\n{title}\n")

    for i, row in enumerate(board):
        print(f"\t{row[0]:^3}|{row[1]:^3}|{row[2]:^3}")
        if i < 2 :
            print(f"\t-----------")

    print('')

def place_on_board(char,place):
    global board
    row = int(math.floor(place / 3))
    col = place % 3
    print_debug(f"row: {row}, col: {col}")
    board[row][col] = char

def read_user_input() :
    global board
    ask_for_input = True
    while ask_for_input :
        yourinput = input("Feed me a number from 1 to 9: ")
        if yourinput == 'q':
            print("Thank you for playing!")
            exit()
        elif yourinput == 'h':
            print_help()
            continue
        elif (not yourinput.isdigit()) :
            print("Oh come on.")
            continue

        yournumber = int(yourinput)-1

        if yournumber > 8 or yournumber < 0:
            print("Number out of range.")
            continue

        place_on_board(yourinput, yournumber)
        print_board()

read_user_input()