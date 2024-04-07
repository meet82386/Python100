import random

heads, tails = 0, 0
for _ in range(400):
    coin = random.randint(0,1)
    if coin == 0:
        heads += 1
        print("Head")
    else:
        tails += 1
        print("Tail")

print(f"Total Heads: {heads}, and Tails: {tails}")