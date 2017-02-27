#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/thomas/gr/Tutorial/gr-tutorial/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/thomas/gr/Tutorial/gr-tutorial/build/python:$PATH
export LD_LIBRARY_PATH=/home/thomas/gr/Tutorial/gr-tutorial/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/thomas/gr/Tutorial/gr-tutorial/build/swig:$PYTHONPATH
/usr/bin/python2 /home/thomas/gr/Tutorial/gr-tutorial/python/qa_multiply_py_ff.py 
