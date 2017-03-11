#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/thomas/gr/gr-test/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/thomas/gr/gr-test/build/python:$PATH
export LD_LIBRARY_PATH=/home/thomas/gr/gr-test/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/thomas/gr/gr-test/build/swig:$PYTHONPATH
/usr/bin/python2 /home/thomas/gr/gr-test/python/qa_square_ff.py 
