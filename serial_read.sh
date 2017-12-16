#!/bin/bash
SERIAL=/home/pi/serial-arduino
pgrep -f SerialReadToStomp.py || python3 $SERIAL/SerialReadToStomp.py > $SERIAL/fermenter.log &
