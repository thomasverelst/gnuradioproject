/* -*- c++ -*- */

#define TEST_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "test_swig_doc.i"

%{
#include "test/test.h"
%}


%include "test/test.h"
GR_SWIG_BLOCK_MAGIC2(test, test);
