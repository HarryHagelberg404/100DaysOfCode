# Hangman psuedo code:
# Generate a random word
# Generate as many blanks as letters in the word
# The user guesses a letter
# Is the guessed letter in the word? Yes / No

# Y Replace the blank with the letter
# Y Are all blanks filled?
#   Y GAME OVER
#   N The user keeps guessing

# N Lose a life
# N Have the user run out of lives?
#   Y GAME OVER
#   N The user keeps guessing

# ------- START OF FILE -------
import random
# Generate a random word:

def generate_word():
    word_list = ["sweden", "denmark", "norway", "finland", "iceland", "new zealand"]
    return word_list[random.randint(0, len(word_list) - 1)]

def word_to_hidden(word):
    hidden_word = ""
    blank = "-"
    space = " "
    for index in range(0, len(word)):
        letter = word[index]
        if letter == space:
            hidden_word += space
        hidden_word += blank
    return hidden_word


def ask_user(hidden_word):
    valid_input = False
    user_input = ""
    print("\nThis is the word your trying to figure out:")
    print(f"{hidden_word}\n")
    while not valid_input:
        user_input = str(input("Please guess a letter that the hidden word may contain:\n")).lower()
        if user_input.isalpha():
            valid_input = True
    return user_input

def isMatch(guessedLetter, choosen_word):
    for index in range(0, len(choosen_word)):
        existingLetter = choosen_word[index]
        if guessedLetter == existingLetter:
            return True
    return False


def redraw_word(guessedLetter, choosen_word, hidden_word):
    new_hidden_word = ""
    blank = "-"
    space = " "
    for index in range(0, len(choosen_word)):
        existingLetter = choosen_word[index]
        if existingLetter == guessedLetter:
            new_hidden_word += guessedLetter
        elif hidden_word[index] == existingLetter:
            #This means this letter has been guessed previously
            new_hidden_word += existingLetter
        elif existingLetter == space:
            new_hidden_word += space
        else:
            new_hidden_word += blank
    return new_hidden_word


def game_winner(isWin):
    msg = ""
    if isWin:
        msg = "YOU WON. You guessed the word!"
    else:
        msg = "YOU LOST. You ran out of lives!"

    valid_input = False
    while not valid_input:
        print(msg)
        user_input = str(input("\nDo you want to play again? Y/N\n")).lower()
        if user_input == "y":
            print(True)
            return start_game()
        elif user_input == "n":
            exit()


def start_game():
    user_lifes = 3
    choosen_word = generate_word()
    hidden_word = word_to_hidden(choosen_word)

    print("Welcome to HANGMAN!\nDo you have what it takes to beat me?")
    # Initialize game loop
    game_alive = True
    while game_alive:
        letter = ask_user(hidden_word)
        if not isMatch(letter, choosen_word):
            user_lifes -= 1
        hidden_word = redraw_word(letter, choosen_word, hidden_word)
        if user_lifes == 0 or hidden_word == choosen_word:
            game_alive = False

    print(f"The word was: {choosen_word}")
    if user_lifes == 0:
        game_winner(False)
    elif hidden_word == choosen_word:
        game_winner(True)


start_game()

