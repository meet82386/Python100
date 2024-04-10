def isPrime(number):
    for _ in range(2, number):
        if number%_ == 0:
            return False
    return True

num = int(input("Enter number to check: "))

if isPrime(num):
    print("Number is prime")
else:
    print("Number is not prime")