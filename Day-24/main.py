PLACEHOLDER = "[NAME]"

with open("names.txt", "r") as names_file:
    names = names_file.readlines()
    print(names)

with open("letter.txt", 'r') as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)

        with open(f"./output/{stripped_name}.txt", 'w') as new_file:
            new_file.write(new_letter)
