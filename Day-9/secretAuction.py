import os

logs = dict()

def find_highest(logs):
    max = 0
    person = ""
    for i in logs:
        if logs[i] > max:
            person = i
            max = logs[i]
    
    return {"name": person, "amount": logs[person]}

    

while True:
    name = input("Enter your name: ")
    amount= int(input("Enter Amount: ").strip('$'))

    logs[name] = amount

    cont = input("Is there any other bid? type 'yes' or 'no': ")
    if cont != 'yes':
        break
    else:
        os.system('cls')

highest_bid = find_highest(logs)
print(f"Winner is: {highest_bid['name']} by {highest_bid['amount']}")