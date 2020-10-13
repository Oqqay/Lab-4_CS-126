# Lenin Valdivia - lav243@nau.edu
# Regan Kalvelage - rnk33@nau.edu
import random


def main():
    print("Welcome to Lights Out!")
    square = solvableSquare()
    solved = solvedSquare()
    movesMade = 0
    for row in square:  # displays generated square
        print("")
        for col in row:
            if col == "\N{WHITE SQUARE}":
                print("\N{WHITE SQUARE} ", end="")
            else:
                print("\N{BLACK SQUARE} ", end="")
    while square != solved:
        print("")
        row = int(input("Choose a row number(0-4): "))
        collum = int(input("Choose a column number(0-4): "))
        puzzle(row, collum, square)
        for row in square:
            print("")
            for col in row:
                if col == "\N{WHITE SQUARE}":
                    print("\N{WHITE SQUARE} ", end="")
                else:
                    print("\N{BLACK SQUARE} ", end="")
        movesMade += 1
        print("")
        print("Moves so far: " + str(movesMade))
    print("Congratulations! You won in " + str(movesMade) + " moves!")
    option = input("Play again? (Type 'y' or 'n'): ").lower()
    if option == 'y' or option == 'yes':
        main()
    else:
        print("Oh well, hope to see you again soon! Goodbye!")
        return movesMade

# The unicodes and strings for the white and black blocks when printed
# from a list are essentially the same thing. We could replace the unicodes
# below with the strings '□' and '■', then just make sure to print out
# the unicodes instead in the main function. But for consistency's sake,
# we're gonna keep using the unicode bellow here aswell.


def puzzle(inRow, inColl, square):
    selection = square[inRow][inColl]

    if selection == "\N{WHITE SQUARE}":
        square[inRow][inColl] = "\N{BLACK SQUARE}"
    elif selection == "\N{BLACK SQUARE}":
        square[inRow][inColl] = "\N{WHITE SQUARE}"

    if inRow == 0:  # Edge cases
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

    return square


def solvableSquare():
    blank = solvedSquare()
    for _ in range(random.randint(15, 50)):  # randomize for random # of times
        row = random.randrange(0, 5)
        col = random.randrange(0, 5)
        blank = puzzle(row, col, blank)
    return blank


def solvedSquare():
    x = "\N{WHITE SQUARE}"
    square = [[x, x, x, x, x],
              [x, x, x, x, x],
              [x, x, x, x, x],
              [x, x, x, x, x],
              [x, x, x, x, x]]
    return square


def opposite(block):
    if block == "\N{WHITE SQUARE}":
        block = "\N{BLACK SQUARE}"
    else:
        block = "\N{WHITE SQUARE}"
    return block


main()
