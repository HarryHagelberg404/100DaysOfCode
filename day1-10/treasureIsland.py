# Treasure Island
input_number = int(input("What number would you want to check for odd or even?"))

num_modulo = input_number % 2

if num_modulo == 0:
    print("Even number")
elif num_modulo == 1:
    print("Odd number")
