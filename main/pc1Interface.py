# Interface for PC1 and PC1's Arduino through serial communication.
# -borBier[21/11/2018]

# "Pull the sleeve up, and fuck it up."

# Library and dependencies.
import time
import serial



# ===== List serial ports. =====
def listSerialPorts():
    result = []
    ports = []
    for i in range(256):
        ports.append('COM%s' % (i + 1))
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result



# ===== Main =====
# List available ports.
status = 'S'

availablePort = listSerialPorts()
print("===== Available Serial Ports =====")
for i, s in enumerate(availablePort):
    print(str(i) + ' ' + s)

# Connect to serial port.
selectedPort = int(input("Select COM port by index >> "))
try:
    ser = serial.Serial(port=availablePort[selectedPort], baudrate=9600,timeout=10)
    print('connected!')
    print(ser.inWaiting())
except serial.serialutil.SerialException:
    print('Exception occured during connecting to COM',selectedPort)

# Sending and Recieving loop.
while True:
    if status == 'S':
        print('===  Sending phase  ===')
        message = input('Send some message : ')

        if message == 'Q':
            break
        elif message != "":
            # Write message to serial. 
            ser.write(message.encode('utf-8'))
            print('Send >> ',message)
            time.sleep(1.0)

            status = 'R'
    elif status == 'R':
        print('=== Recieving Phase ===')
        payload = ""
        
        # Read the serial.
        while payload == "":
            payload = ser.readline()
            print('Waiting for incoming payload. . . ')
            time.sleep(0.1)

        if payload == 'Q':
            break
        elif payload != "":
            # Display payload
            print(payload.decode('utf-8'))
            status = 'S'