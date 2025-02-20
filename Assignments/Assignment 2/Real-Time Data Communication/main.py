import time
import serial

arduinoData = serial.Serial('/dev/cu.usbmodem14301', 9600)
time.sleep(1)

while True:
    while arduinoData.inWaiting() == 0:
        pass
    
    dataPacket = arduinoData.readline()
    dataPacket = str(dataPacket, 'utf-8')
    dataPacket = dataPacket.strip('\r\n')
    splitPacket = dataPacket.split(",")

    #print(dataPacket)
    x = float(splitPacket[0])
    y = float(splitPacket[1])
    z = float(splitPacket[2])

    print("X=", x, "Y=", y, "Z=", z)
