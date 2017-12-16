# simulate fermentation readings

from stompy.simple import Client
from datetime import datetime
import random
from array import array
import time
import json

# open the JMS Client using STOMP protocol
stomp = Client(host='54.201.254.241', port=61613)
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
    stamp = datetime.now().__str__() # get timestamp
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
    msg = {'avg': round(average,2), 'target': round(target,2), 'min': round(min,2), 'max': round(max,2), 'timestamp': stamp }
    print( json.dumps(msg))

    # put message on queue
    stomp.put(msg, destination="/queue/test-queue", persistent=True)
    
    time.sleep(1) # sleep for 1 sec

    
