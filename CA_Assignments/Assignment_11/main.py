import serial
import time

SERIAL_PORT = "COM10" # Change as needed
BAUD_RATE = 9600

def read_uart():
    # Read one byte from UART and prints in correct bit order.

    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout = 2)
        ser.reset_input_buffer()

        print("\nListening for FPGA response...")

        # Read 1 byte
        response = ser.read(1)

        if len(response) == 1:
            received_byte = response[0] # Convert to integer
            received_binary = format(received_byte, '08b') # Convert to binary

            print(f"Raw Byte Received: {response}")
            print(f"Received from FPGA (HEX Format): 0x{received_byte:02X}")
            print(f"Received from FPGA (Binary Format): {received_binary}")
    
        else:
            print("No valid response  recieved.")
        
        ser.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        input("\n Press ENTER to read FPGA data...")
        read_uart()
