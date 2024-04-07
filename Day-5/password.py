import random

print("Welcome to Password generator.")

lenght = int(input("How long do you want your password? \n"))
symb = int(input("How many symbols do you like? \n"))
nums = int(input("How many numbers do you like? \n"))

chars = "qwertyuiopasdfghjklzxcvbnmMNBVCXZASDFGHJKLPOIUYTREWQ"
symbols = "!@~`#$%^&*()"
numbers = "1234567890"

if symb + nums <= lenght:
    pwd = []
    for i in range(symb):
        lenght -= 1
        pwd.append(symbols[random.randint(0, len(symbols)-1)])
    
    for i in range(nums):
        lenght -= 1
        pwd.append(numbers[random.randint(0, len(numbers)-1)])


    for i in range(lenght):    
        pwd.append(chars[random.randint(0, len(chars)-1)])

    random.shuffle(pwd)
    pwd = "".join(pwd)

    print(f"Your generated password is: {pwd}")        
else:
    print("Invalid inputs.") 