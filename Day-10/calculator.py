def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b 

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

acc = 0
op1 = float(input("Enter operand 1: "))
op2 = float(input("Enter operand 2: "))
oper = input("Enter operation +, -, *, / : ")

acc = operations[oper](op1, op2)

print(f"{op1} {oper} {op2} = {acc}")


response = input("Continue calculation? 'yes' or 'no': ")
while response == "yes":
    op1 = acc
    op2 = float(input("Enter operand : "))
    oper = input("Enter operation +, -, *, / : ")

    acc = operations[oper](op1, op2)

    print(f"{op1} {oper} {op2} = {acc}")
    response = input("\nContinue calculation? 'yes' or 'no': ")

    