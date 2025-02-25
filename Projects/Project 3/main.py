import cv2  # Import OpenCV for image processing
import mediapipe as mp  # Import MediaPipe for hand tracking
import serial  # Import serial library for communication with Arduino
import time  # Import time library for delays

# Initialize serial communication with Arduino
arduino = serial.Serial('/dev/cu.usbmodem14101', 9600)  # Set up serial connection with specified port and baud rate
time.sleep(2)  # Wait 2 seconds to allow the connection to establish

# Initialize OpenCV and MediaPipe
cam = cv2.VideoCapture(0)  # Open the default webcam (device index 0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # Set the webcam frame width to 1280 pixels
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Set the webcam frame height to 720 pixels
hands = mp.solutions.hands.Hands()  # Create a MediaPipe Hands object for hand detection
mpDraw = mp.solutions.drawing_utils  # Get drawing utilities for visualizing hand landmarks

# Track previous finger states to avoid redundant serial commands
previous_states = {
    "index": False,  # Initial state of the index finger (not raised)
    "middle": False,  # Initial state of the middle finger
    "ring": False,  # Initial state of the ring finger
    "little": False,  # Initial state of the little finger
    "thumb": False  # Initial state of the thumb
}

while True:
    success, frame = cam.read()  # Capture a frame from the webcam
    if not success:  # Check if the frame was captured successfully
        print("Error: Frame not read!")  # Print an error message if the frame is not read
        break  # Exit the loop

    frame = cv2.flip(frame, 1)  # Flip the frame horizontally for a mirrored effect
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert the frame to RGB (MediaPipe uses RGB format)
    results = hands.process(frameRGB)  # Process the frame using MediaPipe Hands to detect hand landmarks

    if results.multi_hand_landmarks:  # Check if hand landmarks are detected
        for handLms in results.multi_hand_landmarks:  # Loop through each detected hand
            mpDraw.draw_landmarks(frame, handLms, mp.solutions.hands.HAND_CONNECTIONS)  # Draw hand landmarks on the frame

            # Get landmark positions for all fingers
            landmarks = handLms.landmark  # Store detected landmarks
            fingers = {  # Determine if each finger is raised (tip is above the PIP joint)
                "index": landmarks[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].y < 
                         landmarks[mp.solutions.hands.HandLandmark.INDEX_FINGER_PIP].y,
                "middle": landmarks[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP].y < 
                          landmarks[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_PIP].y,
                "ring": landmarks[mp.solutions.hands.HandLandmark.RING_FINGER_TIP].y < 
                        landmarks[mp.solutions.hands.HandLandmark.RING_FINGER_PIP].y,
                "little": landmarks[mp.solutions.hands.HandLandmark.PINKY_TIP].y < 
                          landmarks[mp.solutions.hands.HandLandmark.PINKY_PIP].y,
                "thumb": landmarks[mp.solutions.hands.HandLandmark.THUMB_TIP].y < 
                         landmarks[mp.solutions.hands.HandLandmark.THUMB_IP].y
            }

            # Print the Y-coordinates of all fingers
            print("Y-coordinates of fingers:")
            print(f"Index Finger: {landmarks[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].y}")
            print(f"Middle Finger: {landmarks[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP].y}")
            print(f"Ring Finger: {landmarks[mp.solutions.hands.HandLandmark.RING_FINGER_TIP].y}")
            print(f"Pinky Finger: {landmarks[mp.solutions.hands.HandLandmark.PINKY_TIP].y}")
            print(f"Thumb Finger: {landmarks[mp.solutions.hands.HandLandmark.THUMB_TIP].y}")
            print("\n")

            # Check each finger's state and send commands only if state has changed
            if fingers["index"] and not previous_states["index"]:
                arduino.write(b"led1_on\n")  # Turn on LED 1 if index finger is raised
            elif not fingers["index"] and previous_states["index"]:
                arduino.write(b"led1_off\n")  # Turn off LED 1 if index finger is lowered

            if fingers["middle"] and not previous_states["middle"]:
                arduino.write(b"led2_on\n")  # Turn on LED 2 if middle finger is raised
            elif not fingers["middle"] and previous_states["middle"]:
                arduino.write(b"led2_off\n")  # Turn off LED 2 if middle finger is lowered

            if fingers["ring"] and not previous_states["ring"]:
                arduino.write(b"led3_on\n")  # Turn on LED 3 if ring finger is raised
            elif not fingers["ring"] and previous_states["ring"]:
                arduino.write(b"led3_off\n")  # Turn off LED 3 if ring finger is lowered

            if fingers["little"] and not previous_states["little"]:
                arduino.write(b"led4_on\n")  # Turn on LED 4 if little finger is raised
            elif not fingers["little"] and previous_states["little"]:
                arduino.write(b"led4_off\n")  # Turn off LED 4 if little finger is lowered

            if fingers["thumb"] and not previous_states["thumb"]:
                arduino.write(b"leds_off\n")  # Turn off all LEDs if the thumb is raised

            # Update previous finger states
            previous_states = fingers.copy()

    # Display the video feed with hand landmarks
    cv2.imshow("Webcam Feed with Hands", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit the loop if 'q' is pressed
        break

# Release webcam and close OpenCV windows
cam.release()  # Release the webcam resource
cv2.destroyAllWindows()  # Close all OpenCV windows
arduino.close()  # Close the serial connection with Arduino
