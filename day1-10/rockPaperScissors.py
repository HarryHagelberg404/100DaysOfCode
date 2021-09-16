import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

ai_choice = random.randint(0, 2)

valid_choices = ["Rock", "Paper", "Scissors"]

if user_choice == ai_choice:
    print(f"It's a tie! you both choose: {valid_choices[user_choice]}")
elif valid_choices[user_choice] == "Rock" and valid_choices[ai_choice] == "Scissors":
    print(f"You won! Your: {valid_choices[user_choice]} beats the AI's: {valid_choices[ai_choice]}")
elif valid_choices[user_choice] == "Scissors" and valid_choices[ai_choice] == "Paper":
    print(f"You won! Your: {valid_choices[user_choice]} beats the AI's: {valid_choices[ai_choice]}")
elif valid_choices[user_choice] == "Paper" and valid_choices[ai_choice] == "Rock":
    print(f"You won! Your: {valid_choices[user_choice]} beats the AI's: {valid_choices[ai_choice]}")
elif valid_choices[ai_choice] == "Rock" and valid_choices[user_choice] == "Scissors":
    print(f"You lost! Your: {valid_choices[user_choice]} looses to the AI's: {valid_choices[ai_choice]}")
elif valid_choices[ai_choice] == "Scissors" and valid_choices[user_choice] == "Paper":
    print(f"You lost! Your: {valid_choices[user_choice]} looses to the AI's: {valid_choices[ai_choice]}")
elif valid_choices[ai_choice] == "Paper" and valid_choices[user_choice] == "Rock":
    print(f"You lost! Your: {valid_choices[user_choice]} looses to the AI's: {valid_choices[ai_choice]}")

# TODO, Make into object that has its name as first key then the item it beats as its value.
