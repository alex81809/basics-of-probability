import random

def dice_game():
    print("Rolling a dice...")
    dice_faces = [1, 2, 3, 4, 5, 6]
    roll = random.choice(dice_faces)
    print(f"You rolled a {roll}.")
    if roll == 6:
        print("The game can be started!")
    else:
        print("Roll again.")
