## 5. If Statement

# 1. Ask the user to input a number
number = float(input("Enter a number: "))  # Prompts the user to input a number and converts it to a float for comparison

# 2. Check whether the number is positive, negative, or zero
if number > 0:  # Checks if the number is greater than 0
    print("The number is positive.")  # Prints a message if the number is positive

elif number < 0:  # Checks if the number is less than 0
    print("The number is negative.")  # Prints a message if the number is negative

else:  # Executes if the number is neither greater nor less than 0 (it must be zero)
    print("The number is zero.")  # Prints a message if the number is zero