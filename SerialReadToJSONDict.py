# simple program to read from Arduino serial port
# read to a JSON array

import serial
import json
import datetime

# initalise the serial port
ser = serial.Serial('/dev/ttyACM0', 9600)

# set up the data dictionaries
avgs = dict()
mins = dict()
maxs = dict()

# read serial forever
while True:
    temperatureControlData = json.loads(ser.readline()) # read serial into JSON
##    print(temperatureControlData['avg'])
    stamp = datetime.datetime.now() # timestamp
    avgs[stamp] = temperatureControlData['avg'] # add avg to dict
    mins[stamp] = temperatureControlData['min'] # add min to dict
    maxs[stamp] = temperatureControlData['max'] # add max to dict

    print( len(avgs) )

    if len(avgs) >= 10: # when we have 60 mins of data
        # send data to plotly

        print(avgs.values())

        avgs.clear()
        mins.clear()
        maxs.clear()
        
        
        
        
    
