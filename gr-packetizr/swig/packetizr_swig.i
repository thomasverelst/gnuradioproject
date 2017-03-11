/* -*- c++ -*- */

#define PACKETIZR_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "packetizr_swig_doc.i"

%{
#include "packetizr/packet_encoder.h"
%}


%include "packetizr/packet_encoder.h"
GR_SWIG_BLOCK_MAGIC2(packetizr, packet_encoder);
