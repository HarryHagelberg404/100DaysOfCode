# Password Generator

highscores = input("Write a list of highscores separated by ' ':s down below:\n").split()

top_highscore = 0
for n in range(0, len(highscores)):
    curr_score = int(highscores[n])
    if curr_score > top_highscore:
        top_highscore = curr_score

print("The list of highscores:")
print(highscores)
print(f"The highest score:{top_highscore}")
