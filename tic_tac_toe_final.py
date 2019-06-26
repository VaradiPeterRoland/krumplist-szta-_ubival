import os
import random


def print_board():
    boardCells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("–"*13)
    print("|", boardCells[0], "|", boardCells[1], "|", boardCells[2], "|")
    print("–"*13)
    print("|", boardCells[3], "|", boardCells[4], "|", boardCells[5], "|")
    print("–"*13)
    print("|", boardCells[6], "|", boardCells[7], "|", boardCells[8], "|")
    print("–"*13)
    return boardCells

def selection_1(boardCells):

    letter = user_see = int(input("Choose a number for x on the board:"))
    computer_see = user_see - 1
    if boardCells[computer_see] == "x" or "o":
        print("Please choose another cell")

        boardCells[computer_see] = "x"
        print_board()
    return letter

def win_condition(letter,boardCells):
    if boardCells[0] == "x" and boardCells[1] == "x" and boardCells[2] == "x":
            print("player 1 won")
            playtime = False
        elif boardCells[3] == "x" and boardCells[4] == "x" and boardCells[5] == "x" :
            print("player 1 won")
            playtime = False
        elif boardCells[6] == "x" and boardCells[7] == "x" and boardCells[8] == "x" :
            print("player 1 won")
            playtime = False
        elif boardCells[0] == "x" and boardCells[3] == "x" and boardCells[6] == "x" :
            print("player 1 won")
            playtime = False
        elif boardCells[1] == "x" and boardCells[4] == "x" and boardCells[7] == "x" :
            print("player 1 won")
            playtime = False
        elif boardCells[2] == "x" and boardCells[5] == "x" and boardCells[8] == "x" :
            print("player 1 won")
            playtime = False
        elif boardCells[2] == "x" and boardCells[4] == "x" and boardCells[6] == "x" :
            print("player 1 won")
            playtime = False
        elif boardCells[0] == "x" and boardCells[4] == "x" and boardCells[8] == "x" :
            print("player 1 won")
            playtime = False
        elif boardCells[0] == "o" and boardCells[1] == "o" and boardCells[2] == "o" :
            print("player 2 won")
            playtime = False
        elif boardCells[3] == "o" and boardCells[4] == "o" and boardCells[5] == "o" :
            print("player 2 won")
            playtime = False
        elif boardCells[6] == "o" and boardCells[7] == "o" and boardCells[8] == "o" :
            print("player 2 won")
            playtime = False
        elif boardCells[0] == "o" and boardCells[3] == "o" and boardCells[6] == "o" :
            print("player 2 won")
            playtime = False
        elif boardCells[1] == "o" and boardCells[4] == "o" and boardCells[7] == "o" :
            print("player 2 won")
            playtime = False
        elif boardCells[2] == "o" and boardCells[5] == "o" and boardCells[8] == "o" :
            print("player 2 won")
            playtime = False
        elif boardCells[2] == "o" and boardCells[4] == "o" and boardCells[6] == "o" :
            print("player 2 won")
            playtime = False
        elif boardCells[0] == "o" and boardCells[4] == "o" and boardCells[8] == "o" :
            print("player 2 won")
            playtime = False

def main ():
    playtime = True
    print("Welcome Players!!!")


    print_board()

    while playtime:
        print("turn of player 1")
        selection_1(boardCells)
        print("turn of player2")
        selection_2(boardCells)
