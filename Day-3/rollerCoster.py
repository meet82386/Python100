height = int(input("Enter height: "))

if height > 120:
    age = int(input("Enter your age: "))
    if age <= 16:
        print("Please pay $10")
    elif age <= 20:
        print("Please pay $20")
    else:
        print("Please pay $40")

else:
    print("Sorry, wait for one more year to ride.")