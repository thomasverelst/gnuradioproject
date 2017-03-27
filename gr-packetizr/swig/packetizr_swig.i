/* -*- c++ -*- */

#define PACKETIZR_API
#define DIGITAL_API
#define FILTER_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "packetizr_swig_doc.i"

%{
#include "packetizr/packet_encoder.h"
#include "gnuradio/digital/constellation.h"
#include "gnuradio/digital/packet_header_default.h"
#include <gnuradio/digital/api.h>
#include <gnuradio/tagged_stream_block.h>
#include <gnuradio/digital/constellation.h>
#include <gnuradio/block.h>
#include <gnuradio/filter/firdes.h>
#include <gnuradio/filter/pfb_arb_resampler.h>
#include <gnuradio/digital/packet_header_default.h>
#include "packetizr/tagged_stream_demux_xx.h"
%}


%include "packetizr/packet_encoder.h"
%include "gnuradio/digital/constellation.h"
%include "gnuradio/filter/firdes.h"
%include "gnuradio/filter/pfb_arb_resampler.h"
%include "gnuradio/digital/packet_header_default.h"
GR_SWIG_BLOCK_MAGIC2(packetizr, packet_encoder);
%include "packetizr/tagged_stream_demux_xx.h"
GR_SWIG_BLOCK_MAGIC2(packetizr, tagged_stream_demux_xx);
