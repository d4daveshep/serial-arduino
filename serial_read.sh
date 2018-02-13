#!/bin/bash
DIR=/home/pi/development/serial-arduino
SCRIPT=SerialReadToElastic.py
CONFIG_FILE=fermenter.cfg
LOG=elastic.log

# run the above script if it's not running
pgrep -f $SCRIPT || nohup python3 $DIR/$SCRIPT $DIR/$CONFIG_FILE >> $DIR/$LOG 2>&1


