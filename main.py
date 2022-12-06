print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
a = str(input("You\'re at a crossroad. Where do you want to go? Left or Right?\n")).lower()

if a == "left":
    b = input('You have come to a lake. There is a island in the middle of the lake.Do you want to wait for a '
              'boat or swim across? Type "wait" to wait for a boat or \n"swim" to swim across.\n').lower()

    if b == "wait":
        c = input("You have arrived the island safely. There is a house with three doors. One red, one blue and "
                  "one yellow. Which do you choose?\n").lower()

        if c == "yellow":
            print("You have found the treasure. You win.")
        elif c == "blue":
            print("You are attacked by beasts. Game Over.")
        elif c == "red":
            print("You are exposed to poison. Game Over.")
        else:
            print("You are burned to death for your stupidity. Game Over")

    elif b == "swim":
        print("You are attacked by a shark. Game Over.")
    else:
        print("You are burned to death for your stupidity. Game Over")

elif a == "right":
    print("You fell into a hole. Game Over.")

else:
  print("You are burned to death for your stupidity. Game Over")