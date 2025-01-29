# Importing the threading module for creating and managing threads
import threading

# Importing the time module for adding delays (e.g., time.sleep())
import time

# Defining the Rectangle class
class Rectangle: 
    
    # def      - Defines the constructor method for the class.
    # __init__ - Special method in Python, it is automatically called when you create a new instance of a class.
    # self     - This is the first parameter in all instance methods of a class. It refers to the current instance of the class (the specific object being created).

    # Constructor to initialize a rectangle object with length and width
    def __init__(self, length: float, width: float):
        self.length = length  # Assign the input value to the length attribute
        self.width = width    # Assign the input value to the width attribute

    # Method to calculate and return the area of the rectangle
    def area(self) -> float: 
        return self.length * self.width  # Area formula: length * width
    
    # Method to calculate and return the perimeter of the rectangle
    def perimeter(self) -> float: 
        return 2 * (self.length + self.width)  # Perimeter formula: 2 * (length + width)
    
# Function to process a rectangle object
def process_rectangle(rectangle: Rectangle):  
    # Print the rectangle's area
    print(f"Perimeter of Rectangle ({rectangle.length} x {rectangle.width}): {rectangle.perimeter()}")

# Create multiple Rectangle objects with specified dimensions
rect1 = Rectangle(10, 5)  # Rectangle 1 with length 10 and width 5
rect2 = Rectangle(6, 3)   # Rectangle 2 with length 6 and width 3
rect3 = Rectangle(8, 4)   # Rectangle 3 with length 8 and width 4

# Create an empty list to store threads
threads = []

# Loop through the rectangles to create and start threads
for rect in [rect1, rect2, rect3]:  # Iterate over the list of Rectangle objects
    # Create a thread to process each rectangle using the process_rectangle function
    thread = threading.Thread(target=process_rectangle, args=(rect,))
    threads.append(thread)  # Add the thread to the threads list
    thread.start()  # Start the thread execution

# Wait for all threads to finish execution
for thread in threads:  # Iterate over the list of threads
    thread.join()  # Wait for the thread to complete its task

# Print a final message once all threads are processed
print("All rectangles processed.")
