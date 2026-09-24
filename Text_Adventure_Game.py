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

confirmation = 0

def are_you_sure():
    """ Active after the user enters an incorrect form of input, asking for confirmation.
    If the incorrect input is validated, the function trips a randomized event and the game ends.
    If not, the user is asked for another input."""
    print()
    confirmation = input("Are you sure about your answer? Yes or No  ")
    print()
    if confirmation == "yes" or confirmation == "Yes" or confirmation == "y" or confirmation == "Y":
        print(random.choice(fail_scenarios))
        fail = 1
        end_game()
        return 1
    else:
        path_chosen = input("Please enter your desired answer:  ")
    pass

def summary():
    """Prints a summary of the game"""
    #Add later
    print("Will later print a summary of the game")
    pass

def end_game():
    """Ends the game when the fail variable is 1"""
    summary()

fail_scenarios = ["Add later 1", "Add later 2", "Add later 3"]

limiter = 0

while True:
    try:
        path_chosen = int(input("There are three paths to choose from, one leads staight into the woods, " \
        "another towards a hut barely visible from the edge of the forest, and one leading around the woodland, " \
        "dissapearing around the trees and hills. \n\nChoose a path: 1, 2, or 3.  "
                                ))
        if path_chosen not in [1,2,3]:
            are_you_sure()
                if are_you_sure == 1:
                    break
            limiter += 1
        if limiter >= 3:
            #Add later
            print("Limit Reached")
            fail = 1
        if fail == 1:
            end_game()
            break
    except ValueError:
        print()
        print("Invalid input. Please enter a number (1, 2, or 3).")
        print()
    if type(path_chosen) == int and (path_chosen in [1,2,3]):
        print()
        print("Loop Complete - Remove/Replace later")
        print()
        break
    else:
        continue

#Path 1 Route

path_1_endings = {1:"Something1", 2: "Something2", 3: "Something3"}   

while path_chosen == 1:
    if fail == 1:
        end_game()
        break
    try:
        path_1 = int(input("Placeholder"))
        if path_1 not in [1,2,3]:
            are_you_sure()
            limiter += 1
        if limiter >= 3:
            #Add later
            print("Limit Reached")
            fail = 1
    except ValueError:
        print()
        print("Invalid input. Please enter a number (1, 2, or 3).")
        print()
    if type(path_1) == int:
        print()
        print("Loop Complete - Remove/Replace later")
        print()
        break
    else:
        continue

#Path 2 Route

path_2_endings = {1:"Something1", 2: "Something2", 3: "Something3"}  

while path_chosen == 2:
    if fail == 1:
        end_game()
        break
    try:
        path_2 = int(input("Placeholder"))
        if path_2 not in [1,2,3]:
            are_you_sure()
            limiter += 1
        if limiter >= 3:
            #Add later
            print("Limit Reached")
            fail = 1
    except ValueError:
        print()
        print("Invalid input. Please enter a number (1, 2, or 3).")
        print()
    if type(path_2) == int:
        print()
        print("Loop Complete - Remove/Replace later")
        print()
        break
    else:
        continue

#Path 3 Route    

path_3_endings = {1:"Something1", 2: "Something2", 3: "Something3"}  

while path_chosen == 3:
    if fail == 1:
        end_game()
        break
    try:
        path_3 = int(input("Placeholder"))
        if path_3 not in [1,2,3]:
            are_you_sure()
            limiter += 1
        if limiter >= 3:
            #Add later
            print("Limit Reached")
            fail = 1
    except ValueError:
        print()
        print("Invalid input. Please enter a number (1, 2, or 3).")
        print()
    if type(path_3) == int:
        print()
        print("Loop Complete - Remove/Replace later")
        print()
        break
    else:
        continue