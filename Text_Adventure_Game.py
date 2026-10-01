"""Name: Text_Adventure_Game
   Author: Elizaveta Maliugina
   Purpose: Project 1 for CSCI 1511
   Date: 9/30/2026
   Resources: None"""

name = str(input("Welcome! Enter your name:  "))

print(f"\nYou arrive at the edge of a forest.")

import random

import sys

def are_you_sure(current_path):
    """ Active after the user enters an incorrect form of input, asking for confirmation.
    If the incorrect input is validated, the function trips a randomized event and the game ends.
    If not, the user is asked for another input."""

    confirmation = input(f"\nAre you sure about your answer? Yes or No  ")

    if confirmation.strip().lower() in ["yes", "y"]:
        print(random.choice(fail_scenarios))
        summary()
    else:
        new_value = int(input(f"\nPlease enter your desired answer:  "))
        return new_value

def summary():
    """Prints a summary and ends the game"""
    print("\n---  Game Summary  ---")
    print(f"Player Name: {name}")
    if marker == 000:
        print("Only got to the forest enterance before indecisiveness caught up.")
    elif marker == 111:
        print("Chose the first of many paths, most of which remain unknown due to indecisiveness.")
    elif marker == 11:
        print("Chose to go into the woods, discovering the ruins and finding the treasures inside.")
    elif marker == 12:
        print("Chose to go into the woods, discovering the ruins, but decided to try and catch up to the entity in the background. Losing sight of the creature, you get stranded in the woods with darkness aproaching.")
    elif marker == 13:
        print("Chose to go into the woods, discovering the ruins, but decided to continue following the path and reaching the wishing tree.")
    elif marker == 222:
        print("Chose to go to the hut, but indecisiveness over the tea led you to a dead end.")
    elif marker == 21:
        print("Chose to go to the hut and accept Beatrice's tea and help, getting a full night's rest and some helpful advice.")
    elif marker == 22:
        print("Chose to go to the hut, but declined Beatrice's offer of tea, leading to you possibly missing out on something interesting.")
    elif marker == 333:
        print("Chose to go around the woods and into the cliff field, but indecisiveness led to your peril.")
    elif marker == 31:
        print("Chose to go around the woods into the cliff field and pick up the cloak and other items, letting you get another interesting item.")
    elif marker == 32:
        print("Chose to go around the woods into the cliff field and do down the frayed rope to discover a cave, where some critters were speaking. Once discovered they left a shell that you collected while avoiding a collapse, continuing your exploration.")
    sys.exit()

fail_scenarios = [f"\nYou walk out forward, intending to step through a pile of leaves, but instead, you fall straight though them into a bottomless pit.",
                f"\nYou hear a whistling sound quickly getting lowder and closer, as you look around, you barely have time to see the object as it lands next to you and *BOOM*",
                f"\nYou hear distantly approaching howls, and are then devoured by a pack of wolves."]

limiter = 0

marker = 0

while True:
    try:
        path_chosen = int(input(f"\nThere are three paths to choose from, one leads staight into the woods, " \
        "another towards a hut barely visible from the edge of the forest, and one leading around the woodland, " \
        "dissapearing around the trees and hills. \n\nChoose a path: 1, 2, or 3.  "
                                ))
        if path_chosen not in [1,2,3]:
            path_chosen = are_you_sure(path_chosen)
            limiter += 1
        if limiter == 2:
            print(f"\nDue to your indecisiveness...")
            print(random.choice(fail_scenarios))
            marker = 000
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
            path_1 = are_you_sure(path_1)
            limiter += 1
        if limiter == 2:
            print(f"\nDue to your indecisiveness...")
            print(random.choice(fail_scenarios))
            marker = 111
            summary()
    except ValueError:
        print(f"\nInvalid input. Please enter a number (1, 2, or 3):  ")
    if type(path_1) == int and (path_1 in [1,2,3]):
        print(f"\nLoop 2 Complete - Remove/Replace later")
        if path_1 == 1:
            print(path_1_endings[1])
            marker = 11
            summary()
        elif path_1 == 2:
            print(path_1_endings[2])
            marker = 12
            summary()
        elif path_1 == 3:
            print(path_1_endings[3])
            marker = 13
            summary()
        break
    else:
        continue

#Path 2 Route

path_2_endings = {1:f"\nYou accept the tea and tell Beatrice, as the old woman introduced herself, about the tales of your travels and what you are looking for. You chat until nightfall, when Beatrice offers to let you stay the night. You accept her offer and spend the night with no issues and in the morning, Beatrice gives you some tips and sends you on your way.",
                2: f"\nYou decline the tea, and Beatrice, as the old woman introduced herself, looked hurt but still heard you out. You tell her what you are looking for, she tells you that you won't find it in this forest and you leave without finding anything."}  

while path_chosen == 2:
    try:
        path_2 = int(input(f"\nAs you slowly appreach the hut, you hear humming comming from within. You knock on the door and an old woman answers."
                           "'Come in,' she says, 'Let's have some tea and you can tell me about your travels.' You go in and inspect the hut; you see various herbs hung among humble interior"
                            "and a cauldron bubbling in the corner over the fire. You sit down at the table in the corner and the old lady offers you the tea, do you drink it?"
                            "\n\nChoose an option: 1 to accept and 2 to decline:  "))
        if path_2 not in [1,2]:
            path_2 = are_you_sure(path_2)
            limiter += 1
        if limiter == 2:
            print(f"\nDue to your indecisiveness...")
            print(random.choice(fail_scenarios))
            marker = 222
            summary()
    except ValueError:
        print(f"\nInvalid input. Please enter a number (1 or 2):  ")
    if type(path_2) == int and (path_2 in [1,2]):
        print(f"\nLoop 3 Complete - Remove/Replace later")
        if path_2 == 1:
            print(path_2_endings[1])
            marker = 21
            summary()
        elif path_2 == 2:
            print(path_2_endings[2])
            marker = 22
            summary()
        break
    else:
        continue

#Path 3 Route    

path_3_endings = {1:f"\nYou pick up the items and put them on. You continue walking along the cliff but soon notice that the animals no longer react to your presence. You keep walking and see a camp with a waving flag and soldiers guarding what seems to be a sort of treasure. After some patient waiting and a perfect moment, you make your way out with the treasure, hearing a commotion beginning in the distance behind you.",
                2: "Climbing down the rope, almost falling and slipping down rocks, you arrive at the entrance of cave on the beach. You enter and begin to hear strange whispers. Eventually, you reach a part of the cave that has a hole for sunlight where you find some creatures having a hushed discussion. They scramble away as they notice you, leaving behind a shiny shell. Just as you pick it up, the cave starts shaking. You barely make it out as the cave collapses behind you and you decide to continue walking and exploring the beach."}  

while path_chosen == 3:
    try:
        path_3 = int(input(f"\nYou proceed around the woods and enter a field leading to a cliffside. There is a herd of wild ungulates grazing and various birds sitting in the trees and on the cliff's edge. "
                           "You walk up to the cliff edge and find some items such as a cloak, dagger, and bag with coins in the tall grass. You also see a rope going down the cliff."
                           "\n\nChoose an option, 1 for picking up the items and 2 for climbing down the rope:  "))
        if path_3 not in [1,2]:
            path_3 = are_you_sure(path_3)
            limiter += 1
        if limiter == 2:
            print(f"\nDue to your indecisiveness...")
            print(random.choice(fail_scenarios))
            marker = 333
            summary()
    except ValueError:
        print(f"\nInvalid input. Please enter a number (1 or 2)  ")
    if type(path_3) == int and (path_3 in [1,2]):
        print(f"\nLoop 4 Complete - Remove/Replace later")
        if path_3 == 1:
            print(path_3_endings[1])
            marker = 31
            summary()
        elif path_3 == 2:
            print(path_3_endings[2])
            marker = 32
            summary()
        break
    else:
        continue