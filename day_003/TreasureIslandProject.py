print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
step_1 = input("Left or Right? ")
if step_1 == "Left" or step_1 == "left":
    step_2 = input("Swim or Wait? ")
    if step_2 == "Wait" or step_2 == "wait":
        step_3 = input("Which door: Red Yellow or Blue? ")
        if step_3 == "Yellow" or step_3 == "yellow":
            print("YOU WIN!")
        elif step_3 == "Red" or step_3 == "red":
            print("Burned by fire. GAME OVER.")
        elif step_3 == "Blue" or step_3 == "blue":
            print("Eaten by beasts. GAME OVER")
        else:
            print("GAME OVER.")
    else:
        print("Attacked by trout. GAME OVER.")
else:
    print("Fall into a hole. GAME OVER.")