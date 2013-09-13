"""
Ex 3 for Hackbright Academy

What I want to do: 
	Repeat forever:
	-read user input
	-if they enter 'q', quit the program. Otherwise, separate their input into parts.
	-First part is the operator.  
	-If operator is a binary arithmetic operation, turn remaining two parts into integers,
	then call the appropriate function.
	-If it's a unary operation, just turn the remaining one part into an integer and call the 
	function.
"""

import arithmetic

def main():
	while True: #repeat forever
		user_input = raw_input(">")
		parts = user_input.split()
		operator = parts[0]

		if operator == "q":
			return
			#Stop looping, exit the function
		elif operator == "+":
			num1 = int(parts[1])
			num2 = int(parts[2])
			print arithmetic.add(num1, num2)
		elif operator == "-":
			num1 = int(parts[1])
			num2 = int(parts[2])
			print arithmetic.subtract(num1, num2)
		elif operator == "*":
			num1 = int(parts[1])
			num2 = int(parts[2])
			print arithmetic.multiply(num1, num2)
		elif operator == "/":
			num1 = int(parts[1])
			num2 = int(parts[2])
		elif operator == "pow":
			num1 = int(parts[1])
			num2 = int(parts[2])
			print arithmetic.power(num1, num2)
		elif operator == "square":
			num1 = int(parts[1])
			print arithmetic.square(num1)
		elif operator == "cube":
			num1 = int(parts[1])
			print arithmetic.cub(num1)
		else:
			print "I don't know why you're trying to do."

if __name__ == "__main__":
	main()
