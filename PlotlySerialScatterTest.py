# test plotly

import datetime
import serial
import json
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

#tls.set_credentials_file(username='daveshep', api_key='benvu2ol6q')
ser = serial.Serial('/dev/ttyACM0', 9600)
while True:
##    print(ser.readline())
    parsed_json = json.loads(ser.readline())
    print(parsed_json['avg'])

    timestamp=datetime.datetime.now()

    traceAvg = go.Scatter(
        x=timestamp,
        y=parsed_json['avg'],
        mode='lines+markers',
        name='avg'
        )
    traceMin = go.Scatter(
        x=timestamp,
        y=parsed_json['min'],
        mode='lines+markers',
        name='min'
        )
    traceMax = go.Scatter(
        x=timestamp,
        y=parsed_json['max'],
        mode='lines+markers',
        name='max'
        )

    data = [traceAvg,traceMin,traceMax]

    py.plot(data, filename='scatter test', fileopt='extend', privacy='public')
    



                         
