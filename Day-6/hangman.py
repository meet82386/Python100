import random
import assets

print(assets.asciiArt)

wrong_guesses = 0
right_guesses = 0
animal = assets.words[random.randint(0, len(assets.words)-1)]
word = ['_'] * len(animal)

while(right_guesses != len(animal) and wrong_guesses < len(assets.HANGMANPICS)):
    print("".join(word))
    print(animal)
    guess = input("Guess the word: ").lower()[0]

    if guess in animal:
        ind = animal.index(guess)
        string_list = list(animal)
        string_list[ind] = '-'
        animal = "".join(string_list)
        word[ind] = guess
        print("Right guess")
        print(f"The word was: {word}")
        right_guesses += 1
    else:
        print("Wrong guess")
        print(assets.HANGMANPICS[wrong_guesses])
        wrong_guesses += 1

if right_guesses == len(animal):
    print("Hurray!, You gueesed the word.")
else:
    print("It's okay, Good luck next time.")



