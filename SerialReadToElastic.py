# simple program to read from Arduino serial port

import serial
import json
import glob
from datetime import datetime
import time
import elasticsearch
from elasticsearch import Elasticsearch

# connect to Elasticsearch
eshost = 'search-test-fermenter-temp-ac27nb3jxwgsv6m6zfpjpsprsa.us-west-2.es.amazonaws.com' 
#es = Elasticsearch(
#    hosts=[{'host':eshost, 'port':443}],
#    use_ssl=True,
#    verify_certs=True,
#    sniff_on_start=True,
#    sniffer_timeout=60,
#    sniff_on_connection_fail=True,
#    connection_class=elasticsearch.connection.RequestsHttpConnection
#)
#print( es.cluster.health() )

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

time.sleep(30) # sleep for 30 secs to allow arduino to reboot

while True:
    line = ser.readline() # read serial line as bytes
#    print(line.decode('utf-8'))
    data = json.loads(line.decode('utf-8')) # convert serial line to string and load to JSON
    stamp = datetime.now() # get timestamp and format with 0 millisecs

    data['timestamp'] = stamp.strftime('%Y-%m-%dT%H:%M:%S.0+13')
#    data['brewid'] = '12-AAA-02'
    data['brewid'] = '99-TEST-99'

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
    
