def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


print("Enter two numbers for operations")
a = int(input("Number1: "))
b = int(input("Number2: "))
operation = input("Operation (+, -, %, *): ")

if operation == "+":
    print(add(a, b))
elif operation == "-":
    print(sub(a, b))
elif operation == "*":
    print(div(a, b))
elif operation == "*":
    print(mul(a, b))
else:
    print("operation not supported")
