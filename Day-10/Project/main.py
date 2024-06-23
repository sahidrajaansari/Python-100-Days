# calculator
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))
while True:
    operation = input("What operation do you want? +, -, *, /: ")
    if operation == "+":
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif operation == "*":
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif operation == "/":
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid operation")  
        break
    num1 = result
    want_to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if want_to_continue == 'y':
        num2 = int(input("What's the next number?: "))
    else:
        num1 = int(input("What's the first number?: "))
        num2 = int(input("What's the second number?: "))
        continue
