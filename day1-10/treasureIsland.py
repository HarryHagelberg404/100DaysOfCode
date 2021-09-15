# Treasure Island
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
user_input = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")

if user_input == "left":
    user_input = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if user_input == "wait":
        user_input = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
        if user_input == "red":
            print("The room contains a hidden trap. GAME OVER")
        elif user_input == "yellow":
            print("The room contains the treasure. YOU WIN")
        elif user_input == "blue":
            print("You enter a room full of beasts. GAME OVER")
    elif user_input == "swim":
        print("There is a foul creature in the water. GAME OVER")
elif user_input == "right":
    print("This road is used by bandits. GAME OVER")
