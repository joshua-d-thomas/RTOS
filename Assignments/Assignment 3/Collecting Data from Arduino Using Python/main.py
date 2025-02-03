import time
import serial

# Replace with your actual serial port (check in Arduino IDE)
arduinoData = serial.Serial('/dev/cu.usbmodem14101', 9600)

time.sleep(2)  # Allow time for the connection to establish

while True:
    # print(type(arduinoData.in_waiting))
    if arduinoData.in_waiting == 0: 
        break
        
    dataPacket = arduinoData.readline()
    # print(f"debug: {dataPacket}")

    dataPacket = dataPacket.decode('utf-8').strip()  # Read and clean the data
    potValue = int(dataPacket)  # Convert to integer
    
    print("Potentiometer Value:", potValue)

    time.sleep(0.5)

arduinoData.close()  # Ensure the serial connection is properly closed
