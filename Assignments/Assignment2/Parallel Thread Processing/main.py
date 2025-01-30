from threading import Thread
from time import sleep

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

def process_rectangle(rectangle):
    print(f"Rectangle ({rectangle.width}x{rectangle.height}) Area: {rectangle.area()}")
    sleep(2)  # Simulates a delay
    print(f"Rectangle ({rectangle.width}x{rectangle.height}) Perimeter: {rectangle.perimeter()}")

# Creating multiple Rectangle objects
rectangles = [Rectangle(10, 5), Rectangle(7, 3), Rectangle(6, 8), Rectangle(12, 4)]

# Creating and starting multiple threads
threads = []
for rect in rectangles:
    thread = Thread(target=process_rectangle, args=(rect,))
    threads.append(thread)
    thread.start()

# Waiting for all threads to complete
for thread in threads:
    thread.join()

print("All rectangles processed.")
