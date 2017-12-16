# simple program to read from Arduino serial port
# read to a JSON array

import serial
import json
import datetime
import collections
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

# initalise the serial port
ser = serial.Serial('/dev/ttyACM1', 9600)

# set up the data dictionaries
avgs = collections.OrderedDict()
mins = collections.OrderedDict()
maxs = collections.OrderedDict()
aims = collections.OrderedDict()

# read serial forever
while True:
    temperatureControlData = json.loads(ser.readline()) # read serial into JSON
##    print(temperatureControlData['avg'])
    stamp = datetime.datetime.now() # timestamp
    avgs[stamp] = temperatureControlData['avg'] # add avg to dict
    mins[stamp] = temperatureControlData['min'] # add min to dict
    maxs[stamp] = temperatureControlData['max'] # add max to dict
    aims[stamp] = temperatureControlData['target'] # add target to dict

    print( len(avgs) )
    print( temperatureControlData )

    if len(avgs) >= 60: # when we have 60 mins of data
        
        # send data to plotly
        traceAvg = go.Scatter(
            x=avgs.keys(),
            y=avgs.values(),
            mode='lines',
            name='avg'
        )
        traceMin = go.Scatter(
            x=mins.keys(),
            y=mins.values(),
            mode='lines',
            name='min'
        )
        traceMax = go.Scatter(
            x=maxs.keys(),
            y=maxs.values(),
            mode='lines',
            name='max'
        )
        traceAim = go.Scatter(
            x=aims.keys(),
            y=aims.values(),
            mode='lines',
            name='target'
        )

        data = [traceAvg,traceMin,traceMax,traceAim]

        layout = go.Layout( title = 'Brew APA3',
              yaxis = dict(title='temp'),
              xaxis = dict(title='time')
        )

        fig = go.Figure(data=data, layout=layout)

        py.plot(fig, filename='brew apa3', fileopt='extend', privacy='public')

        print(avgs.values())

        avgs.clear()
        mins.clear()
        maxs.clear()
        aims.clear()
        
        
        
        
    
