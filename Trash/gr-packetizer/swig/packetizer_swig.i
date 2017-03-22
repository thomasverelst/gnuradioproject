/* -*- c++ -*- */

#define PACKETIZER_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "packetizer_swig_doc.i"

%{
#include "packetizer/packet_encoder_bc.h"
%}

%include "packetizer/packet_encoder_bc.h"
GR_SWIG_BLOCK_MAGIC2(packetizer, packet_encoder_bc);
