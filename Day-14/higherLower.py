from random import randint
from game_data import data

# Function to get information about random instagram account
def getCeleb():
    '''Get random insta account from list.'''
    random_number = randint(0, len(data)-1)
    return data[random_number]

score = 0
predicted_right = True

acc1 = getCeleb()

while predicted_right:
    acc2 = getCeleb()

    print(f"{acc1.get('name')} ({acc1.get('description')}) V/S {acc2.get('name')} ({acc2.get('description')})")

    guess = input("Type A to high and B to low: ").upper()

    if guess == 'A':
        # Check if account 2 has high score than account 1 or not?
        if acc1.get('follower_count') <= acc2.get('follower_count'):
            print("You are right.")
            score += 1
        else:
            predicted_right = False

    elif guess == 'B':
        # Check if account 2 has low score than account 1 or not?
        if acc1.get('follower_count') <= acc2.get('follower_count'):
            print("You are right.")
            score += 1
        else:
            predicted_right = False

    else:
        print("Invalid input.")
        predicted_right = False

    acc1 = acc2



print("Sorry, wrong answer.")
print(f"Game terminated, Your score is {score}")