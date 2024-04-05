print("Welcome to the tip calculator")

amount = float(input("What was the total bill? "))
tip_perc = int(input("How much tip you want to give? 10, 12 or 15? "))
people = int(input("How many people to split the bills? "))

total_price = amount + (amount * tip_perc / 100)
share = total_price / people

print(f"Each person should pay: INR {share}")