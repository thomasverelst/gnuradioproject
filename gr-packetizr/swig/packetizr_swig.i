/* -*- c++ -*- */

#define PACKETIZR_API
#define DIGITAL_API
#define FILTER_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "packetizr_swig_doc.i"

%{
#include "packetizr/packet_encoder.h"
#include "gnuradio/top_block.h"
#include "gnuradio/digital/constellation.h"
#include "gnuradio/digital/packet_header_default.h"
#include <gnuradio/digital/api.h>
#include <gnuradio/tagged_stream_block.h>
#include <gnuradio/digital/constellation.h>
#include <gnuradio/block.h>
#include <gnuradio/digital/packet_header_default.h>
#include "packetizr/tagged_stream_demux_xx.h"
#include "packetizr/preamble_header_payload_demux.h"
#include "packetizr/tagged_whitener.h"
#include "packetizr/whitener.h"
%}


%include "packetizr/packet_encoder.h"
%include "gnuradio/digital/constellation.h"
%include "gnuradio/digital/packet_header_default.h"
%include "gnuradio/top_block.h"
GR_SWIG_BLOCK_MAGIC2(packetizr, packet_encoder);
%include "packetizr/tagged_stream_demux_xx.h"
GR_SWIG_BLOCK_MAGIC2(packetizr, tagged_stream_demux_xx);

%include "packetizr/preamble_header_payload_demux.h"
GR_SWIG_BLOCK_MAGIC2(packetizr, preamble_header_payload_demux);

%include "packetizr/tagged_whitener.h"
GR_SWIG_BLOCK_MAGIC2(packetizr, tagged_whitener);
%include "packetizr/whitener.h"
//GR_SWIG_BLOCK_MAGIC2(packetizr, whitener);
