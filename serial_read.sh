#!/bin/bash
DIR=/home/pi/development/serial-arduino
SCRIPT=SerialReadToElastic.py
LOG=elastic.log

# run the above script if it's not running
pgrep -f $SCRIPT || nohup python3 $DIR/$SCRIPT >> $DIR/$LOG 2>&1


