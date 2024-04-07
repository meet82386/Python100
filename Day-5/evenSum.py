end = int(input("Enter number to stop: "))
sum = 0

for i in range(2, end+1, 2):
    sum += i

print(f"Your sum is: {sum}")