# test plotly

import plotly.plotly as py
import plotly.tools as tls
#import plotly.graph_objs as go
from plotly.graph_objs import *
import datetime

tls.set_credentials_file(username='daveshep', api_key='benvu2ol6q', stream_ids=['479jskn39w'])

# get my stream ids
stream_ids = tls.get_credentials_file()['stream_ids']
stream_id = stream_ids[0]

# create a stream id object
stream = Stream(
    token=stream_id,
    maxpoints=80
    )

# create the scatter plot
trace1 = Scatter(
    x=[],
    y=[],
    mode='line+markers',
    stream=stream
    )

data = Data([trace1])
layout = Layout(title='Test')
fig = Figure(data=data, layout=layout)
url = py.plot(fig,filename='stream test', privacy='public')

# open the stream
s = py.Stream(stream_id)
s.open()

# stream some data

#while True:
    # write the data to plotly
#s.write(dict(x=datetime.datetime.now(), y=123.45))
#s.write(dict(x=123,y=456))
s.write({'x':123,'y':456},validate=True)

s.close()
#time.sleep(1.0)
    

    
