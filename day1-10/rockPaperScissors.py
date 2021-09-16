import random

if random.randint(0, 1) == 1:
    coin_state = "Heads"
else:
    coin_state = "Tails"

print(f"The coin flipped to a: {coin_state}")
