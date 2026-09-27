"""Name: Text_Adventure_Game
   Author: Elizaveta Maliugina
   Purpose: Project 1 for CSCI 1511
   Date: 9/27/2026 """

name = str(input("Welcome! Enter your name:  "))

print(f"\nYou arrive at the edge of a forest.")

import random

import sys

fail = 0

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
        summary()
        #Figure out value to end game
    else:
        path_chosen = input("Please enter your desired answer:  ")

def summary():
    """Prints a summary of the game, can also end game if fail = 1"""
    #Add later
    print(f"\nWill later print a summary of the game")
    sys.exit()

fail_scenarios = [f"\nYou walk forward, intending to step through a pile of leaves, but instead, you fall straight though them into a bottomless pit.",
                f"\nYou hear a whistling sound quickly getting lowder and closer, as you look around, you barely have time to see the object as it lands next to you and *BOOM*",
                f"\nYou hear distantly approaching howls, and are then devoured by a pack of wolves."]

limiter = 0

while True:
    try:
        path_chosen = int(input(f"\nThere are three paths to choose from, one leads staight into the woods, " \
        "another towards a hut barely visible from the edge of the forest, and one leading around the woodland, " \
        "dissapearing around the trees and hills. \n\nChoose a path: 1, 2, or 3.  "
                                ))
        if path_chosen not in [1,2,3]:
            are_you_sure()
            limiter += 1
        if limiter == 3:
            print(f"\nDue to your indecisiveness...")
            fail = 1
        if fail == 1:
            summary()
            break
    except ValueError:
        print("\nInvalid input. Please enter a number (1, 2, or 3).")
    if type(path_chosen) == int and (path_chosen in [1,2,3]):
        print(f"\nLoop 1 Complete - Remove/Replace later")
        break
    else:
        continue

#Path 1 Route

marker = 0

path_1_endings = {1:f"\nYou explore the ruins and as the sun begins setting, their glow becomes clearer. You find an unlocked chest with a symbol on the front and open it to find the riches of your dreams.",\
                2: f"\nYou try to follow whatever is moving, but it soon outruns you and you find yourself lost as the sun sets.",\
                3: f"\nYou ignore the ruins and the creature as you continue down the path. As you reach the end of the path, you see strange flore and fauna beginning to take over."
                "You reach the elder tree that you were after, using one of its branches to make a wish."}   

while path_chosen == 1:
    try:
        path_1 = int(input(f"\nYou walk directly into the woods. You continue for what seems like forever until you arrive at some mysteryous ruins, their faint glow seems to pull you towards them."
                        "Out of the corner of your eye, you something move in the forest. The path continues to the side of the ruins."
                        "\n\nChoose a path: 1, 2 or 3:  "))
        if path_1 not in [1,2,3]:
            are_you_sure()
            limiter += 1
        if limiter == 3:
            print(f"\nDue to your indecisiveness...")
            fail = 1
    except ValueError:
        print(f"\nInvalid input. Please enter a number (1, 2, or 3):  ")
    if type(path_1) == int:
        print(f"\nLoop 2 Complete - Remove/Replace later")
        if path_1 == 1:
            print(path_1_endings[1])
            summary()
        elif path_1 == 2:
            print(path_1_endings[2])
            summary()
        elif path_1 == 3:
            print(path_1_endings[3])
            summary()
        break
    else:
        continue

#Path 2 Route

path_2_endings = {1:"Something1", 2: "Something2", 3: "Something3"}  

while path_chosen == 2:
    try:
        path_2 = int(input("Placeholder"))
        if path_2 not in [1,2,3]:
            are_you_sure()
            limiter += 1
        if limiter == 3:
            print(f"\nDue to your indecisiveness...")
            fail = 1
    except ValueError:
        print(f"\nInvalid input. Please enter a number (1, 2, or 3):  ")
    if type(path_2) == int:
        print(f"\nLoop 3 Complete - Remove/Replace later")
        break
    else:
        continue

#Path 3 Route    

path_3_endings = {1:"Something1", 2: "Something2", 3: "Something3"}  

while path_chosen == 3:
    try:
        path_3 = int(input("Placeholder"))
        if path_3 not in [1,2,3]:
            are_you_sure()
            limiter += 1
        if limiter == 3:
            print(f"\nDue to your indecisiveness...")
            fail = 1
    except ValueError:
        print(f"\nInvalid input. Please enter a number (1, 2, or 3):  ")
    if type(path_3) == int:
        print(f"\nLoop 4 Complete - Remove/Replace later")
        break
    else:
        continue