class Rectangle:
    
    # def      - Defines the constructor method for the class.
    # __init__ - Special method in Python, it is automatically called when you create a new instance of a class.
    # self     - This is the first parameter in all instance methods of a class. It refers to the current instance of the class (the specific object being created).
    
    def __init__(self, length: float, width: float):
        # Initialize the Rectangle with length and width.
        self.length = length
        self.width = width

    def area(self) -> float:
        # Calculate and return the area of the rectangle.
        return self.length * self.width

    def perimeter(self) -> float:
        # Calculate and return the perimeter of the rectangle.
        return 2 * (self.length + self.width)

    def resize(self, factor: float):
        # Multiply the length and width by the given factor
        self.length *= factor
        self.width *= factor
        
# Create two Rectangle objects with different dimensions
rect1 = Rectangle(10, 5)
rect2 = Rectangle(6, 3)

# Print area, perimeter, and resized dimensions of both rectangles
print("Rectangle 1:")
print("Area:", rect1.area())  # Output: 50
print("Perimeter:", rect1.perimeter())  # Output: 30

rect1.resize(2)  # Resizing rectangle 1 by a factor of 2
print("Resized Dimensions (Rectangle 1) - Length:", rect1.length, "Width:", rect1.width)
print("Resized Area (Rectangle 1):", rect1.area())  # Output: 200
print("Resized Perimeter (Rectangle 1):", rect1.perimeter())  # Output: 60

print("\nRectangle 2:")
print("Area:", rect2.area())  # Output: 18
print("Perimeter:", rect2.perimeter())  # Output: 18

rect2.resize(3)  # Resizing rectangle 2 by a factor of 3
print("Resized Dimensions (Rectangle 2) - Length:", rect2.length, "Width:", rect2.width)
print("Resized Area (Rectangle 2):", rect2.area())  # Output: 54
print("Resized Perimeter (Rectangle 2):", rect2.perimeter())  # Output: 36


