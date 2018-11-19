# Library and dependencies.
import serial
import time

# Configuration stuffs.
captureTime = 20.0
cmdList = ["capture"]

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

# List the ports.
availablePort = listSerialPorts()
print("===== Available Serial Ports =====")
for i, s in enumerate(availablePort):
    print(str(i) + ' ' + s)

# Connect to serial port.
selectedPort = int(input("Select COM port by index >> "))
ser = serial
try:
    ser = serial.Serial(port=availablePort[selectedPort], baudrate=115200,timeout=10)
    print('connected!')
    print(ser.inWaiting())
except serial.serialutil.SerialException:
    print('Exception occured during connecting to COM',selectedPort)

# Recieving command.
while True:
    command = ser.read_until('\n').decode('utf-8')
    print(command)
    time.sleep(1000)