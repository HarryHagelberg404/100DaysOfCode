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
word_list = ["Sweden", "Denmark", "Norway", "Finland", "Iceland", "New Zealand"]
word = word_list[random.randint(0, len(word_list) - 1)]

word = "New Zealand"

# Generate the equal amount of letters as blanks
hidden_word = ""
blank = "-"
space = " "
for index in range(0, len(word)):
    letter = word[index]
    if letter == space:
        hidden_word += space
    hidden_word += blank


print(word)
print(hidden_word)

# Ask the user to guess a letter:


# Check if the letter exists:


