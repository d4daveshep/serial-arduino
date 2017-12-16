# test plotly

import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *

tls.set_credentials_file(username='daveshep', api_key='benvu2ol6q')

py.plot({                      # use `py.iplot` inside the ipython notebook
    "data": [{
        "x": [1, 2, 3],
        "y": [4, 2, 5]
    }],
    "layout": {
        "title": "hello world"
    }
}, filename='hello world',      # name of the file as saved in your plotly account
   privacy='public')            # 'public' | 'private' | 'secret': Learn more: https://plot.ly/python/privacy


                         
