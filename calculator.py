while True:
	num1 = float(input("Enter first number: "))
	num2 = float(input("Enter second number: "))
	op = input("Enter operation (+, -, *, /): ")
	if op == "exit":
		print("Goodbye!")
		break
	if op == "+":
		result = num1 + num2
	elif op == "-":
		result = num1 - num2
	elif op == "*":
		result = num1 * num2
	elif op == "/":
		if num2 != 0:
			result = num1 / num2
		else:
			print("Cannot divide by zero")
			continue
	else:
		print("Invalid operation")
		continue
	print("Result:",result)
