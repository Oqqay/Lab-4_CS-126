# Lenin Valdivia - lav243@nau.edu
# Regan Kalvelage
import random

def main():
    pass    #print("Welcome to Lights Out: a puzzle where you are given a grid of
     #     lights, with some dark and others light. You must turn them all off by
      #    clicking on the cells. Each click toggles that cell and each of its
       #   immediate neighbors.")
    # this is where generating a solvable square func will go

def x():
    y = random.randint(0, 1)
    return y
def solvableSquare():
    # x = random.randint(0, 1)
    square = [[x(), x(), x(), x(), x()],
              [x(), x(), x(), x(), x()],
              [x(), x(), x(), x(), x()],
              [x(), x(), x(), x(), x()], 
              [x(), x(), x(), x(), x()]]
    print(square)

solvableSquare()
