# simple program to read from Arduino serial port

import serial
import json
import glob
from datetime import datetime
from stomp import *
import time

# open the JMS Client using STOMP protocol
stomp = Connection([('54.201.254.241', 61613)],auto_content_length=False) # auto_content_length=False sets the message type to TextMessage
stomp.set_listener('', PrintingListener())
stomp.start()
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

time.sleep(30) # sleep for 30 secs to allow arduino to reboot

while True:
    line = ser.readline() # read serial line as bytes
#    print(line.decode('utf-8'))
    data = json.loads(line.decode('utf-8')) # convert serial line to string and load to JSON
    stamp = datetime.now() # get timestamp
    data['timestamp'] = stamp.__str__()
    data['brewid'] = '12-AAA-02'
#    data['brewid'] = '99-TEST-99'

    msg = data
    print( json.dumps(msg) )

    # put message on queue
    stomp.send('/queue/test-queue', json.dumps(msg), headers={'persistent': 'true'})
