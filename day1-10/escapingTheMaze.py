# Escaping the maze
# The code that was written inside the website
# NOTE. that theese are predefined functions inside the website.
# NOTE. that this code does not take regard to the edge case of when the robot is spawned in a void containing no wall to the right.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()


