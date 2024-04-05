num = input("Enter your number: ")
sum = 0

for i in num:
    int_digit = int(i)
    sum += int_digit

print(f"Sum of characters is: {sum}")