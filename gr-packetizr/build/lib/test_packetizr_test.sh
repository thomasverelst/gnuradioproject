#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/thomas/gr/gr-packetizr/lib
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/thomas/gr/gr-packetizr/build/lib:$PATH
export LD_LIBRARY_PATH=/home/thomas/gr/gr-packetizr/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-packetizr 