print("Welcome to Treasure Island.\nYour mission is to find the treasure\nYou're at the cross road. Where do you want to go?\n")
direction = input("Type 'Left' or 'Right'?: ").lower()
if direction == "left":
    swim_or_wait = input("Swim or Wait ").lower()
    if swim_or_wait == "wait":
        door = input("Which door?\nRed, Blue or Yellow? ").lower()
        if door == "red":
            print("Burned by fire.\n Game Over")
        elif door == "blue":
            print("Eaten by beasts.\n Game Over")
        elif door == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\n Game Over.")
else:
    print("Fall into a hole.\nGame Over.")