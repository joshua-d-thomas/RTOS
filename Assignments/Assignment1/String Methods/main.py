## 2. String Methods

# Define the string
text = "python programming"  # Assigns the string "python programming" to the variable `text`

# 1. Convert the string to uppercase
uppercase_text = text.upper()  # Converts all characters in `text` to uppercase using the `upper()` method

# 2. Replace the word "programming" with "language"
replaced_text = text.replace("programming", "language")  # Replaces "programming" with "language" using the `replace()` method

# 3. Count the occurrences of the letter "p" in the string (case-sensitive)
p_count = text.count("p")  # Counts how many times the character "p" appears in `text` using the `count()` method

# Print the results
print(f"Uppercase: {uppercase_text}")  # Prints the result of the uppercase conversion
print(f"Replaced: {replaced_text}")    # Prints the string after replacing "programming" with "language"
print(f"Occurrences of 'p': {p_count}")  # Prints the number of times "p" appears in the original string
