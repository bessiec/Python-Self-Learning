#Doing some CodeAcademy exercises to keep up with my coding as I'm in grad school

#Making a single-p Battleship game

#importing randint
from random import randint 

#creating empty list to make gameboard
board = []

#creating gameboard of Os
for x in range(0, 5):
    board.append(["O"] * 5)

#creating a function to print out board with just "Os" to look pretty
def print_board(board):
    for row in board:
        print " ".join(row)

#creating functions to choose random location on board
def random_col(board):
    return randint(0, len(board) - 1) #we do this because board starts 0, 1, 2...

def random_row(board):
    return randint(0, len(board[0]) -1) #we do this because board starts 0, 1, 2... 

#player actions
for turn in range(4): #four chances to guess
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        print_board(board)
        break
    else:
        if guess_row < 0 or guess_row > len(board)-1 or guess_col < 0 or guess_col > len(board[0]) - 1:
            print "Oops, that's not even in the ocean."
            print_board(board)
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already."
            print_board(board)
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
    print "You taken %s turns" % str(turn+1)
    if turn == 3:
            print "Game Over"
  


