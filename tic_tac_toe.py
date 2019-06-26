import random


def inputPlayerLetter():
    letter = ""
    while letter != "X" or letter != "O":
        print("You want to be X or O")
        letter = input().upper()
    if letter == "x":
        return ["X", "O"]
    if letter == "O":
        return ["O", "X"]

def WhoGoesFirst():
    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"

def play_again():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")
def 