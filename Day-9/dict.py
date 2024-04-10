dictionary = {
    "Name": "Meet Thummar",
    "Age": 20,
    "Quote": "Sixtenn hours work is good!"
}

print(f"A famous {dictionary['Age']} year old Philosopher {dictionary['Name']} told {dictionary['Quote']}")

for i in dictionary:
    print(i)
    print(dictionary[i])