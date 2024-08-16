import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')


def generate():
    name = input("Enter your name: ").upper()
    try:
        nato_list = [data.code[data.letter == char].values[0] for char in name if char != ' ']
    except IndexError:
        print("Invalid Input String.")
        generate()
    else:
        print(" ".join(nato_list))


generate()
