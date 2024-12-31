# Program to divide two numbers
num1 = int(input("Enter the numerator: "))
num2 = int(input("Enter the denominator: "))

if num2 != 0:
    # Dividing the numbers
    division = num1 / num2
    print(f"The division of {num1} by {num2} is {division}.")
else:
    print("Error: Division by zero is not allowed.")
