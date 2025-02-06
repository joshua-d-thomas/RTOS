import cv2

print(cv2.__version__)

# Initialize webcam
cam = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    ret, frame = cam.read()
    if not ret:
        break

    # Convert to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the color feed
    cv2.imshow('Color Feed', frame)
    cv2.moveWindow('Color Feed', 0, 0)

    # Display the grayscale feed
    cv2.imshow('Grayscale Feed', gray_frame)
    cv2.moveWindow('Grayscale Feed', 700, 0)  # Adjusted position for Mac

    # Press 'q' to exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
