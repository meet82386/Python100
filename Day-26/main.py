import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
name = input("Enter your name: ").upper()
NATO_list = [data.code[data.letter == char].values[0] for char in name if char != ' ']

print(" ".join(NATO_list))

