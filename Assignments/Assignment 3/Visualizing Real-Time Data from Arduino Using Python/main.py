import time
import serial
from vpython import *

arduinoData = serial.Serial('/dev/cu.usbmodem14101', 9600)

time.sleep(1)

tube = cylinder(color = color.blue, radius = 1, length=5, axis = vector(0,1,0))

while True:
    while arduinoData.in_waiting == 0:
        pass
    dataPacket=arduinoData.readline()
    print(dataPacket)
    dataPacket2=str(dataPacket,'UTF-8')
    print(dataPacket2)
    dataPacket3=dataPacket2.strip('\r\n')
    print(dataPacket3)
    dataPacket4=int(dataPacket3)
    print(dataPacket4)
    potVal=dataPacket4
    voltage = (float(5/1023))*potVal
    print(voltage)
    voltage2=round(voltage,2)
    print(voltage2)
    if voltage == 0:
        voltage = 0.001
    tube.length=voltage


