# Treasure Island
input_year = int(input("What year want you check if it's a leap year?\n"))

year_divided = input_year / 4

if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            print("Leap year!")
        else:
            print("Not a leap year!")
    else:
            print("Leap year!")
else:
    print("Not a leap year!")
