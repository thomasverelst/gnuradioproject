#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/thomas/gr/gr-tutorial/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/thomas/gr/gr-tutorial/build/python:$PATH
export LD_LIBRARY_PATH=/home/thomas/gr/gr-tutorial/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/thomas/gr/gr-tutorial/build/swig:$PYTHONPATH
/usr/bin/python2 /home/thomas/gr/gr-tutorial/python/qa_my_qpsk_demod_cb.py 
