import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    serial_raw = ser.readline()
    print serial_raw
