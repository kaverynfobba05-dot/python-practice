# Learning while loop will understand better in class
while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        print("Result is:", num1 + num2)

    elif operation == "-":
        print("Result is:", num1 - num2)

    elif operation == "*":
        print("Result is:", num1 * num2)

    elif operation == "/":
        print("Result is:", num1 / num2)

    else:
        print("Invalid operation")

    choice = input("Do you want to continue? (yes/no): ")

    if choice == "no":
        print("Calculator stopped")
        break
