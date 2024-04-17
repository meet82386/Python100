import random

print("Welcome to Number Guessing Game.")
print("Range 1 to 100")
mode = input("Choose difficulty: 'easy' or 'hard' ")

attempts = 5
random_number = random.randint(1, 101)
if mode == 'easy':
    attempts = 8

print(f"You have {attempts} attempts to complete game.")
isGuessed = False

while attempts != 0:
    num = int(input("Enter number: "))

    if num == random_number:
        print("You guessed it right... Congretulations!")
        isGuessed = True
        break

    if num > random_number:
        print("Too high guess something less.")
    else:
        print("Too low guess something high.")
    
    attempts -= 1
    print(f"{attempts} attempts remaining.")

if not isGuessed:
    print("\nYou loose")


    