inp = input("Enter Line: ")

char_count = {word: len(word) for word in inp.split()}
print(char_count)
