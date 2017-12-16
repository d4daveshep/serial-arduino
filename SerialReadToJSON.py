# simple program to read from Arduino serial port
# read to a JSON array

import serial
import json

ser = serial.Serial('/dev/ttyACM0', 9600)
while True:
    parsed_json = json.loads(ser.readline())
    print(parsed_json['avg'])
    
