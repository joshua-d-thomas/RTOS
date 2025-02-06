import cv2
import numpy as np

# Get user input
board_size = int(input("Enter the size of the checkerboard (in pixels): "))
num_squares = int(input("Enter the number of squares per row/column: "))

# Calculate the size of each square
square_size = board_size // num_squares

# Create the checkerboard image
checkerboard = np.zeros((board_size, board_size, 3), dtype=np.uint8)

# Loop to fill squares
for row in range(num_squares):
    for col in range(num_squares):
        if (row + col) % 2 == 0:
            color = (0, 0, 0)  # Black
        else:
            color = (0, 255, 0)  # Green

        # Define the square region
        start_x = col * square_size
        start_y = row * square_size
        end_x = start_x + square_size
        end_y = start_y + square_size

        # Fill the square with the color
        checkerboard[start_y:end_y, start_x:end_x] = color

# Display the checkerboard
cv2.imshow('Dynamic Checkerboard', checkerboard)

# Wait until 'q' is pressed to close the window
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()