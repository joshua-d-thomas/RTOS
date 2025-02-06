import cv2
import numpy as np

## Creating Arrays
# Create a 5x5 matrix filled with zeros
frame = np.zeros((5, 5), dtype=np.uint8)
print("Initial 5x5 matrix:\n", frame)

# Create a cross pattern
frame[2, :] = 255   # Horizontal line in the middle
frame[:, 2] = 255   # Vertical line in the middle
print("Matrix with cross pattern:\n", frame)

# Display the matrix as an image
cv2.imshow('Cross Pattern', frame)
cv2.moveWindow('Cross Pattern', 0, 0)


## Playing with Colors
# Create a 250x250 image filled with red
image = np.zeros((250, 250, 3), dtype=np.uint8)
image[:, :] = [0, 0, 255]  # Red (BGR format)

# Modify a portion to green and another portion to blue
image[:, 0:125] = [0, 255, 0]          # Left half green
image[125:250, 125:250] = [255, 0, 0]  # Bottom-right quarter blue (non-overlapping)

# Display the colored image
cv2.imshow('Colored Image', image)
cv2.moveWindow('Colored Image', 300, 0)

# Wait for 'q' key to exit
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
