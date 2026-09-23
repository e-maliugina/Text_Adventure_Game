"""Name: Text_Adventure_Game
   Author: Elizaveta Maliugina
   Purpose: Project 1 for CSCI 1511
   Date: 9/27/2026 """

name = str(input("Welcome! Enter your name:  "))

print()
print("You arrive at the edge of a forest.")
print()

import random

fail = 0

def are_you_sure():
    """ Active after the user enters an incorrect form of input, asking for confirmation. If the incorrect input is validated, the function trips a randomized event and the game ends. If not, the user is asked for another input."""
    print()
    confirmation = input("Are you sure about your answer? Yes or No  ")
    print()
    if confirmation != "yes" or confirmation != "Yes" or confirmation != "y" or confirmation != "Y":
        print(random.choice(fail_scenarios))
        fail = 1
    else:
        path_chosen = input("Please enter your desired answer:  ")
    pass

fail_scenarios = ["Add later 1", "Add later 2", "Add later 3"]

limiter = 0

while True:
    try:
        path_chosen = int(input("There are three paths to choose from, one leads staight into the woods, another towards a hut barely visible from the edge of the forest, and one leading around the woodland, dissapearing around the trees and hills. \n\nChoose a path: 1, 2, or 3.  "))
        if path_chosen not in [1,2,3]:
            are_you_sure()
            limiter += 1
        if limiter >= 3:
            #Add later
            print("Limit Reached")
            break
        if fail == 1:
            break
    except ValueError:
        print()
        print("Invalid input. Please enter a number (1, 2, or 3).")
        print()
    if type(path_chosen) == int:
        print()
        print("Loop Complete - Remove/Replace later")
        print()
        break
    else:
        continue

def end_game():
    """Ends the game when the fail variable is 1"""
    #Add later
    pass

#Path 1 Route       
if path_chosen == 1:
    path_1 = input("Placeholder")
