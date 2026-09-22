name = str(input("Welcome! Enter your name:  "))

print()
print("You arrive at the edge of a forest.")
print()

try:
    path_chosen = int(input("There are three paths to choose from, one leads staight into the woods, another towards a hut barely visible from the edge of the forest, and one leading around the woodland, dissapearing around the trees and hills. \n\nChoose a path: 1, 2, or 3.  "))
except ValueError:
    print()
    path_choosen = input("Try again, enter 1, 2, or 3 for your choosen route.  ")

def are_you_sure():
    """ Active after the user enters an incorrect form of input, asking for confirmation. If the incorrect input is validated, the function trips a randomized event and the game ends. If not, the user is asked for another input."""
    #Add later
    print("'are_you_sure' not added yet")
    pass

if path_choosen != 1 or path_choosen != 2 or path_choosen != 3:
    are_you_sure()

