# use this for building on raspberrypi
#FROM resin/raspberrypi-python:3

# use this for buiding on intel linux
FROM python:3.4

# install and upgrade pip3 so we can install pyserial module
RUN apt-get update && apt-get -y install python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install pyserial

# copy the python files to run
COPY SerialRead.py /tmp/SerialRead.py

# set the file to run when the container starts
ENTRYPOINT ["python3", "/tmp/SerialRead.py"]






