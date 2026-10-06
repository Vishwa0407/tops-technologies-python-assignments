# 5.Create a basic calculator program that takes two numbers and an operator (+, -, *, /) as input, performs the correct operation using typecasting, and prints the result. If the user enters an invalid operator, print an error message.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")


if operator == "+":
    print("+:", num1 + num2)
elif operator == "-":
    print("-:", num1 - num2)
elif operator == "*":
    print("*:", num1 * num2)
elif operator == "/":
    print("/:", num1 / num2)
else:
    print("Error: Invalid operator")