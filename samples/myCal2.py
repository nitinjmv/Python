def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b != 0:
        return a / b
    else:
        raise Exception("second value can not be 0")


print("Enter two Numbers")
a = int(input("Number1: "))
b = int(input("Number2: "))

operation = input("Enter operation (+, -, /, *): ")
match operation:
    case "+":
        result = add(a, b)
    case "-":
        result = sub(a, b)
    case "*":
        result = mul(a, b)
    case "/":
        try:
            result = div(a, b)
        except Exception as e:
            print(e)
    case _:
        print("Operation '{}' not supported.".format(operation))

if result is not None:
    print("{} {} {} = {}".format(a, operation, b, result))
