/* -*- c++ -*- */

#define PACKETIZER_API
#define DIGITAL_API
#define FILTER_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "packetizer_swig_doc.i"

%{
#include "packetizer/packet_encoder.h"
#include "gnuradio/top_block.h"
#include "gnuradio/digital/constellation.h"
#include "gnuradio/digital/packet_header_default.h"
#include <gnuradio/digital/api.h>
#include <gnuradio/tagged_stream_block.h>
#include <gnuradio/digital/constellation.h>
#include <gnuradio/block.h>
#include <gnuradio/filter/firdes.h>
#include <gnuradio/filter/pfb_arb_resampler.h>
#include <gnuradio/digital/packet_header_default.h>
#include <gnuradio/top_block.h>
#include "packetizer/preamble_header_payload_demux.h"
#include "packetizer/tagged_whitener.h"
#include "packetizer/whitener.h"
#include "packetizer/corr_est_cc.h"
#include "packetizer/message_sequence_checker.h"
%}


%include "packetizer/packet_encoder.h"
%include "gnuradio/digital/constellation.h"
%include "gnuradio/filter/firdes.h"
%include "gnuradio/filter/pfb_arb_resampler.h"
%include "gnuradio/digital/packet_header_default.h"
%include "gnuradio/top_block.h"
GR_SWIG_BLOCK_MAGIC2(packetizer, packet_encoder);

%include "packetizer/preamble_header_payload_demux.h"
GR_SWIG_BLOCK_MAGIC2(packetizer, preamble_header_payload_demux);

%include "packetizer/tagged_whitener.h"
GR_SWIG_BLOCK_MAGIC2(packetizer, tagged_whitener);
%include "packetizer/whitener.h"
%include "packetizer/corr_est_cc.h"
GR_SWIG_BLOCK_MAGIC2(packetizer, corr_est_cc);
%include "packetizer/message_sequence_checker.h"
GR_SWIG_BLOCK_MAGIC2(packetizer, message_sequence_checker);
%include "gnuradio/block_gateway.h"

%include "gnuradio/block.h"
%include "gnuradio/tags.h"
