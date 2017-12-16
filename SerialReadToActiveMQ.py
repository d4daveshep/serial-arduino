# simple program to read from Arduino serial port

import serial
import json
import sys
from datetime import datetime
from stompy.simple import Client

# open the JMS Client using STOMP protocol
stomp = Client(host='54.201.254.241', port=61613)
stomp.connect()

# find the serial port
ttylist = glob.glob('/dev/ttyACM*')
if len(ttylist) == 0:
    print( 'ERROR: No Arduino devices found at /dev/ttyACM*' )
    sys.exit()

if len(ttylist) > 1:
    print( 'WARNING: Multiple Arduino devices found at /dev/ttyACM*, using first device' )

tty = ttylist[0]
print( 'INFO: Using Arduino device at ' + tty )

# open the serial port
ser = serial.Serial(tty, 9600)
while True:
    data = json.loads(ser.readline()) # read serial into JSON
    stamp = datetime.now() # get timestamp
    data['timestamp'] = stamp.__str__()

    msg = data
    print msg

    stomp.put(msg, destination="/queue/test-queue")
