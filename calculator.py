def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Cannot divide by zero")
        return None
    return a / b

while True:
	try:
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
	except ValueError:
		print("Invalid input. Please enter numeric values.")
		continue
	
	op = input("Enter operation (+, -, *, /): ")
	
	if op == "exit":
		print("Goodbye!")
		break
	
	if op == "+":
		result = add(num1, num2)
		print("Result:", result)
	elif op == "-":
		result = subtract(num1, num2)
		print("Result:", result)
	elif op == "*":
		result = multiply(num1, num2)
		print("Result:", result)
	elif op == "/":
		result = divide(num1, num2)
		if result is not None:
			print("Result:", result)
	else:
		print("Invalid operation")
