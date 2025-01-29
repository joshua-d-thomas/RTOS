## 4. Arithmetic and Comparison Operators

# 1. Accept two numbers from the user
num1 = float(input("Enter the first number: "))  # Prompts the user to input the first number and converts it to a float
num2 = float(input("Enter the second number: "))  # Prompts the user to input the second number and converts it to a float

# 2. Perform arithmetic operations
addition = num1 + num2  # Adds `num1` and `num2`
subtraction = num1 - num2  # Subtracts `num2` from `num1`
multiplication = num1 * num2  # Multiplies `num1` and `num2`
division = num1 / num2 if num2 != 0 else "undefined"  # Divides `num1` by `num2` (checks to avoid division by zero)

# 3. Compare the two numbers using relational operators
greater = num1 > num2  # Checks if `num1` is greater than `num2`
less = num1 < num2  # Checks if `num1` is less than `num2`
equal = num1 == num2  # Checks if `num1` is equal to `num2`

# Print the results of arithmetic operations
print(f"Addition: {addition}")  # Prints the sum of the two numbers
print(f"Subtraction: {subtraction}")  # Prints the difference between the two numbers
print(f"Multiplication: {multiplication}")  # Prints the product of the two numbers
print(f"Division: {division}")  # Prints the quotient, or "undefined" if dividing by zero

# Print the results of comparisons
print(f"Is the first number greater than the second? {greater}")  # Prints whether `num1` is greater than `num2`
print(f"Is the first number less than the second? {less}")  # Prints whether `num1` is less than `num2`
print(f"Are the two numbers equal? {equal}")  # Prints whether `num1` is equal to `num2`
