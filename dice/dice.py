import random

def roll_dice():
    dice_drawing = {
        1: (
            "┌─────────┐",
            "│         |",
            "│    ●    |",
            "│         |",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      |",
            "│         |",
            "│      ●  |",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ●      |",
            "│    ●    |",
            "│      ●  |",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  |",
            "│         |",
            "│  ●   ●  |",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  |",
            "│    ●    |",
            "│  ●   ●  |",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  |",
            "│  ●   ●  |",
            "│  ●   ●  |",
            "└─────────┘",
        )
    }


    roll = input("Roll the dice? (Y/N): ").lower()
    while True:
        if roll == "y":
            print("Rolling the dice...\n")
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print("dice rolled: {} and {}".format(dice1, dice2))
            # Print dice side by side
            for line1, line2 in zip(dice_drawing[dice1], dice_drawing[dice2]):
                print(f"{line1}  {line2}")
            roll = input("\nRoll the dice again? (Y/N): ").lower()

        elif roll == "n":
            print("Thanks for playing")
            break
        
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            roll = input("Roll the dice? (Y/N): ").lower()


roll_dice()