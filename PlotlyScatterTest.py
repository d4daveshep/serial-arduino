# test plotly

import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
import datetime

#tls.set_credentials_file(username='daveshep', api_key='benvu2ol6q')

timestamp=datetime.datetime.now()

traceAvg = Scatter(
    x=timestamp,
    y=21.34,
    mode='lines+markers',
    name='avg'
    )
traceMin = Scatter(
    x=timestamp,
    y=19.78,
    mode='lines+markers',
    name='min'
    )
traceMax = Scatter(
    x=timestamp,
    y=23.56,
    mode='lines+markers',
    name='max'
    )

data = [traceAvg,traceMin,traceMax]

py.plot(data, filename='scatter test', fileopt='extend', privacy='public')
    



                         
