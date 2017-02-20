#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/thomas/Documents/GR/gr-tutorial/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/thomas/Documents/GR/gr-tutorial/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/thomas/Documents/GR/gr-tutorial/build/swig:$PYTHONPATH
/usr/bin/python2 /home/thomas/Documents/GR/gr-tutorial/python/qa_multiply_py_ff.py 
