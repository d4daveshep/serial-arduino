# simple program to read from Arduino serial port

import serial
import json
import glob
from datetime import datetime
import time
import configparser
import elasticsearch
from elasticsearch import Elasticsearch
import sys
import argparse
from pathlib import Path

# set up the command line parser
parser = argparse.ArgumentParser()

# define the argument to set the config file
parser.add_argument("config_file", help="specify the full location of the config file")

# parse the arguments and check the file exists
args = parser.parse_args()

if args.config_file :
    cfgFile = args.config_file
    print('config file is at...', cfgFile)

    if not Path(cfgFile).exists() :
        print('file NOT found... exiting')
        sys.exit()

# connect to Elasticsearch
eshost = 'search-test-fermenter-temp-ac27nb3jxwgsv6m6zfpjpsprsa.us-west-2.es.amazonaws.com' 

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

# read the target temp from config file
config = configparser.ConfigParser()
config.read(cfgFile)
newTarget = config['temperature']['TargetTemp']
print('target temperature being set to ' + str(newTarget))

time.sleep(30) # sleep for 30 secs to allow arduino to reboot
newTargetString = '<' + str(newTarget) + '>'
ser.write(newTargetString.encode())

while True:
    line = ser.readline() # read serial line as bytes
#    print(line.decode('utf-8'))
    data = json.loads(line.decode('utf-8')) # convert serial line to string and load to JSON
    stamp = datetime.now() # get timestamp and format with 0 millisecs

    data['timestamp'] = stamp.strftime('%Y-%m-%dT%H:%M:%S.0+12') # don't forget to adjust for daylight saving time 
#    data['brewid'] = '12-AAA-02'
    data['brewid'] = '99-TEST-99'

    target = data['target']
    if target != newTarget:
        print( 'target temp ' + str(target) )
        newTargetString = '<' + str(newTarget) + '>'
        ser.write(newTargetString.encode())
        print( 'updated target temp to ' + str(newTarget) )
    

    doc = data
    print( json.dumps(doc) )

    es = Elasticsearch(
        hosts=[{'host':eshost, 'port':443}],
        use_ssl=True,
        verify_certs=True,
        connection_class=elasticsearch.connection.RequestsHttpConnection
    )
    
    # index the doc to elastic
    res = es.index( 
        index="mapping-test", 
        doc_type="brew-temp", 
        body=doc
    )
    print(json.dumps(res))
    
