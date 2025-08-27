Simple Calculator Program

This program asks the user to input two numbers and a mathematical operation
(addition, subtraction, multiplication, or division). It then performs the
operation and prints the result.
"""

# Ask user for the first number
num1 = float(input("Enter the first number: "))

# Ask user for the second number
num2 = float(input("Enter the second number: "))

# Ask user for a mathematical operator
operator = input("Enter an operator (+, -, *, /): ")

# Perform the calculation based on the operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        result = None
    else:
        result = num1 / num2
else:
    print("Error: Invalid operator.")
    result = None

# Display result if calculation was successful
if result is not None:
    print(f"{num1} {operator} {num2} = {result}")