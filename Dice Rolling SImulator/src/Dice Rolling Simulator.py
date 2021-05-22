import random

def dice():
    reroll = "false"
    while reroll != "true":
        dice = random.randint(1,6)
        print(dice)
        roll_again = input("Do you want to reroll? (Y/N): ").lower()
        if roll_again == "y":
            print("Rolling again...")
        else:
            print("Have a nice day!")
            break

roll = "a"
while roll != "roll":
    roll = input("To roll the dice, type roll: ").lower()
    if roll == "roll":
        print("Rolling the dice...")
        dice()
        break

    else:
        print("Wrong Command Typed")