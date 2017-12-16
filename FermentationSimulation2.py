# simulate fermentation readings

#from stompy.simple import Client
from stomp import *
from datetime import datetime
import random
from array import array
import time
import json

# open the JMS Client using STOMP protocol
# auto_content_length=False sets the message type to TextMessage
#stomp = Connection([('54.201.254.241', 61613)],auto_content_length=False)
stomp = Connection([('localhost', 61613)],auto_content_length=False)
stomp.set_listener('', PrintingListener())
stomp.start()
stomp.connect()

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
    stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.0')


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

    #print round(average, 2), round(min,2), round(max,2)

    index += 1 # increment the index
    if index>=N: # reset index if needed
        index=0

    # build json
    msg = {'avg': round(average,2), 'target': round(target,2), 'min': round(min,2), 'max': round(max,2), 'timestamp': stamp, 'brewid': '99-test-99' }
    print( json.dumps(msg))

    # put message on queue
#    stomp.send('/queue/test-queue', json.dumps(msg), headers={'persistent': 'true'})
    stomp.send('/queue/local', json.dumps(msg), headers={'persistent': 'true'})

    time.sleep(60) # sleep for 1 sec

    
