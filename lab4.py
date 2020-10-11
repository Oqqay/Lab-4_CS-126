# Lenin Valdivia - lav243@nau.edu
# Regan Kalvelage
import random

def main():
    print("Welcome to Lights Out!")
    square = solvableSquare()
    solved = solvedSquare()
    movesMade = 0
    for i in range(len(square)):
        print(square[i])
    while square != solved:
        row = int(input("Choose a row number(0-4): "))
        collum = int(input("Choose a collum number(0-4): "))
        puzzle(row, collum, square)
        movesMade += 1


def puzzle(inRow, inColl, square):
    selection = square[inRow][inColl]
    
    if selection == "□":
        square[inRow][inColl] = "■"
    elif selection == "■":
        square[inRow][inColl] = "□"
    right = ""
    left = ""
    up = ""
    down = ""
    if inRow == 0:
        if inColl == 0:
            square[inRow][inColl + 1] = opposite(square[inRow][inColl + 1])
            square[inRow + 1][inColl] = opposite(square[inRow + 1][inColl])
        elif inColl == 4:
            square[inRow][inColl - 1] = opposite(square[inRow][inColl - 1])
            square[inRow + 1][inColl] = opposite(square[inRow + 1][inColl])
        else:
            square[inRow][inColl - 1] = opposite(square[inRow][inColl - 1])
            square[inRow + 1][inColl] = opposite(square[inRow + 1][inColl])
            square[inRow][inColl + 1] = opposite(square[inRow][inColl + 1])
    
    elif inRow == 4:
        if inColl == 0:
            square[inRow][inColl + 1] = opposite(square[inRow][inColl + 1])
            square[inRow - 1][inColl] = opposite(square[inRow - 1][inColl])
        elif inColl == 4:
            square[inRow][inColl - 1] = opposite(square[inRow][inColl - 1])
            square[inRow - 1][inColl] = opposite(square[inRow - 1][inColl])
        else:
            square[inRow][inColl - 1] = opposite(square[inRow][inColl - 1])
            square[inRow - 1][inColl] = opposite(square[inRow - 1][inColl])
            square[inRow][inColl + 1] = opposite(square[inRow][inColl + 1])

    else:
        if inColl == 0:
            square[inRow][inColl + 1] = opposite(square[inRow][inColl + 1])
            square[inRow - 1][inColl] = opposite(square[inRow - 1][inColl])
            square[inRow + 1][inColl] = opposite(square[inRow + 1][inColl])
        elif inColl == 4:
            square[inRow][inColl - 1] = opposite(square[inRow][inColl - 1])
            square[inRow - 1][inColl] = opposite(square[inRow - 1][inColl])
            square[inRow + 1][inColl] = opposite(square[inRow + 1][inColl])
        else:
            square[inRow][inColl + 1] = opposite(square[inRow][inColl + 1])
            square[inRow][inColl - 1] = opposite(square[inRow][inColl - 1])
            square[inRow - 1][inColl] = opposite(square[inRow - 1][inColl])
            square[inRow + 1][inColl] = opposite(square[inRow + 1][inColl])

    for i in range(len(square)):
        print(square[i])
    return square

    

def light():
    light = ["□", "■"]
    return random.choice(light)


def solvableSquare():
    square = [[light(), light(), light(), light(), light()],
              [light(), light(), light(), light(), light()],
              [light(), light(), light(), light(), light()],
              [light(), light(), light(), light(), light()], 
              [light(), light(), light(), light(), light()]]
    return square


def solvedSquare():
    x = "□"
    square = [[x, x, x, x, x],
              [x, x, x, x, x],
              [x, x, x, x, x],
              [x, x, x, x, x],
              [x, x, x, x, x]]
    return square


def opposite(block):
    if block == "□":
        block = "■"
    else:
        block = "□"
    return block


main()
