# simulate fermentation readings

from datetime import datetime
import random
from array import array
import time
import json
import elasticsearch
from elasticsearch import Elasticsearch

# Elasticsearch URL
#eshost = 'search-test-fermenter-temp-ac27nb3jxwgsv6m6zfpjpsprsa.us-west-2.es.amazonaws.com' 
eshost = '192.168.1.55'

N = 50 # number of readings to take an average of
readings = array('f') # the array of readings

total = 0 # the sum of N readings

target = 20 # set the target temp

# initialise the temp readings and calculate the average
for i in range(N):
    temp = random.uniform(target-5,target+5) # get random temp value
    readings.append(temp) # add temp to the array (this grows the array)
    total += temp # add temp to the total

average = total / N # calculate the average temp

# define min and max values and set to average
min = average
max = average

index = 0 # pointer to current reading

while True:
#    stamp = datetime.now().__str__() # get timestamp
    stamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.0+12')

    newtemp = random.uniform(target-5,target+5) # get a new random temp
    oldtemp = readings[index] # remember the temp being replaced by new one
    readings[index] = newtemp # put the new temp in the array
    total = total - oldtemp + newtemp # adjust the total
    average = total / N # calculate the average

    # update the min and max
    if average < min: 
        min = average
    if average > max:
        max = average

    # determine the action
    action = 'Rest'
    rest = True
    heat = False
    cool = False
    
    if average < (target-0.3):
        action = 'Heat'
        heat = True
        rest = False
    if average > (target+0.3):
        action = 'Cool'
        cool = True
        rest = False

    #print round(average, 2), round(min,2), round(max,2)

    index += 1 # increment the index
    if index>=N: # reset index if needed
        index=0

    # build json
    msg = {
        'avg': round(average,2), 
        'action': action, 
        'target': round(target,2), 
        'min': round(min,2), 
        'max': round(max,2), 
        'timestamp': stamp, 
        'brewid': '99-test-99', 
        'now': round(newtemp,2)
    }

    # add action fields
    if rest:
        msg['rest'] = rest
    if heat:
        msg['heat'] = heat
    if cool:
        msg['cool'] = cool

    data = json.dumps(msg)
    print(data)

    # open a connection to elastic
    es = Elasticsearch(
        hosts=[{'host':eshost, 'port':9200}],
#        use_ssl=True,
#        verify_certs=True,
        connection_class=elasticsearch.connection.RequestsHttpConnection
    )

    # index the doc to elastic
    res = es.index( 
        index="brew-temp", 
        doc_type="temp-reading", 
        body=data
    )
    print(json.dumps(res))

    time.sleep(60) # sleep for 1 min
#    time.sleep(1)

    
