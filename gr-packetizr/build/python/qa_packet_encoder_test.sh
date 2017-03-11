#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/thomas/gr/gr-packetizr/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/thomas/gr/gr-packetizr/build/python:$PATH
export LD_LIBRARY_PATH=/home/thomas/gr/gr-packetizr/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/thomas/gr/gr-packetizr/build/swig:$PYTHONPATH
/usr/bin/python2 /home/thomas/gr/gr-packetizr/python/qa_packet_encoder.py 
