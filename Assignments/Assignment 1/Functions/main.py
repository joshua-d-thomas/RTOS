## 10. Functions

# 1. Define a function called square() that takes a number as input and returns its square
def square(num):  # Function `square` that accepts one parameter `num`
    
    return num ** 2  # Returns the square of the input number using exponentiation

# 2. Call the function with a user-provided number and print the result
user_input = float(input("Enter a number: "))  # Prompts the user to input a number and converts it to a float

result = square(user_input)  # Calls the `square` function with the user-provided number

print("The square of", user_input, "is", result)  # Prints the result of squaring the number