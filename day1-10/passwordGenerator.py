# Password Generator
import random

print("Welcome to the PyPassword Generator!\n")
letter_amount = int(input("How many letters in your password would you like?\n"))

symbol_amount = int(input("How many symbols would you like?\n"))

number_amount = int(input("How many numbers would you like?\n"))

letter_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
symbol_array = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '?']
number_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# Creating the password:
def create_passw(amount, char_list):
    # Bad solution with placeholder
    passw = []
    for index in range(amount):
        # Creating:
        passw += add_char(char_list)
    return passw

def add_char(char_list):
    return char_list[random.randint(0, len(char_list) - 1)]

def shuffle_passw(passw):
    for index in range(len(passw)):
        curr_pos = index
        rand_pos = random.randint(0, len(passw) - 1)

        # Basic swap of chars:
        passw[curr_pos], passw[rand_pos] = passw[rand_pos], passw[curr_pos]
    return passw

password = create_passw(letter_amount, letter_array)
password += create_passw(symbol_amount, symbol_array)
password += create_passw(number_amount, number_array)

password = ''.join(shuffle_passw(password))

print(f"Your password has been created and shuffled. Here it is:\n\n{password}")
