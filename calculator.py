num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")
if op == "+":
	result = num1 + num2
if op == "-":
	result = num1 - num2
if op == "*":
	result = num1 * num2
if op == "/":
	result = num1 / num2
print(result)