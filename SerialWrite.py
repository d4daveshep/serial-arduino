# simple program to write to Arduino serial port

import serial
import glob
import sys

ttylist = glob.glob('/dev/ttyACM*')
if len(ttylist) == 0:
    print( 'ERROR: No Arduino devices found at /dev/ttyACM*' )
    sys.exit()

if len(ttylist) > 1:
    print( 'WARNING: Multiple Arduino devices found at /dev/ttyACM*, using first device' )

tty = ttylist[0]
print( 'INFO: Using Arduino device at ' + tty )

ser = serial.Serial(tty, 9600)

ser.write(b'<23.4>')
#ser.write(b'<david>')

while True:
    line = ser.readline()
    print(line.decode('utf-8'))
    
    
    
    
