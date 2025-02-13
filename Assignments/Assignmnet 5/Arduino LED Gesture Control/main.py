import cv2
import mediapipe as mp
import serial  # For Arduino Communication
import time  # To add delays for Arduino initialization

# Initialize serial communication with Arduino
arduino = serial.Serial('/dev/cu.usbmodem14101', 9600)
time.sleep(2)

# Initialize OpenCV and MediaPipe
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
hands = mp.solutions.hands.Hands()
mpDraw = mp.solutions.drawing_utils

# Variables to track LED state
led_on = False

while True:
    success, frame = cam.read()
    if not success:
        print("Error: Frame not read!")
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)

    if results.multi_hand_landmarks:  # Check if hands are detected
        for handLms in results.multi_hand_landmarks:
            # Draw hand landmarks
            mpDraw.draw_landmarks(frame, handLms, mp.solutions.hands.HAND_CONNECTIONS)

            # Get landmarks for index finger (tip and PIP joint)
            index_tip = handLms.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
            index_pip = handLms.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_PIP]

            # Check if index finger is lifted (y-coordinate of tip is less than PIP joint)
            if index_tip.y < index_pip.y:
                if not led_on:  # Turn on LED only if it's currently off
                    arduino.write(b"on\n")  # Send 'on' command to Arduino
                    print("LED turned ON")
                    led_on = True
            else:
                if led_on:  # Turn off LED only if it's currently on
                    arduino.write(b"off\n")
                    print("LED turned OFF")
                    led_on = False

    # Display the video feed
    cv2.imshow("Webcam Feed with Hands", frame)

    # Quit the program if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources after exiting the loop
cam.release()
cv2.destroyAllWindows()
arduino.close()
