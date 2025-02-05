import cv2

print(cv2.__version__)

cam=cv2.VideoCapture(0)

while True:
    ignore, frame = cam.read()
    