import random

row_1 = ["X", "X", "X"]

row_2 = ["X", "X", "X"]

row_3 = ["X", "X", "X"]

map = [row_1, row_2, row_3]

print(f"{row_1}\n{row_2}\n{row_3}")

position = input("Where do you want to put the treasure? ex. 21 for 2 X and 1 Y")

pos_x = position[1]

pos_y = position[0]

selected = map[int(pos_x) - 1][int(pos_y) - 1] = "O"

print(f"{row_1}\n{row_2}\n{row_3}")
