person1 = input("Enter person1 name: ")
person2 = input("Enter person2 name: ")

first_digit = 0
last_digit = 0

for _ in person1:
    if _.lower() in "true":
        first_digit += 1
    if _.lower() in "love":
        last_digit += 1

for _ in person2:
    if _.lower() in "true":
        first_digit += 1
    if _.lower() in "love":
        last_digit += 1

score = first_digit*10 + last_digit

print(f"Love score: {score}")

if score <= 10 and score >= 90:
    print("You are like coke and mentos together.")
elif score >= 40 and score <= 50:
    print("You are alright together")
