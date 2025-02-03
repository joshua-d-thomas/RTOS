import time
import serial
from vpython import *

# Set up serial communication
arduinoData = serial.Serial('/dev/cu.usbmodem14101', 9600)
time.sleep(1)

# Create a VPython cylinder
tube = cylinder(color=color.blue, radius=1, length=5, axis=vector(0, 1, 0))

# Label for displaying voltage value
label_display = label(pos=vector(3, 1, 0), text="0.00V", height=20, box=False)

while True:
    while arduinoData.in_waiting == 0:
        pass

    dataPacket = arduinoData.readline()
    dataPacket3 = dataPacket.decode('utf-8').strip()
    
    try:
        potVal = int(dataPacket3)
        voltage = (5.0 / 1023.0) * potVal
        voltage2 = round(voltage, 2)
    except ValueError:
        continue  # Ignore invalid data

    if voltage <= 0:
        voltage = 0.001  # Prevent zero-length cylinder

    tube.length = voltage
    label_display.text = f"{voltage2} V"
