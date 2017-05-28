#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from gnuradio import digital
import ctypes
#from gnuradio import digital_swig as digital
import packetizer_swig as packetizer

class qa_packet_encoder (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_packet_encoder_bpsk (self):
        preamble = (1,-1,-1,1)
        src_data = (0b11001000,0b01111111,0b01100001,0b11110100)
 
        constel_header   = digital.constellation_calcdist(([1,-1]), ([0, 1]), 2, 1).base()
        constel_payload  = digital.constellation_calcdist(([1,-1]), ([0, 1]), 2, 1).base()
        
        header_formatter = digital.packet_header_default(32/constel_header.bits_per_symbol(), "packet_len", "packet_num", constel_header.bits_per_symbol())
        
        expected_result = preamble + \
        ((1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (-1+0j), (1+0j), (1+0j),
		(1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), 
		(1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j),
		(-1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (1+0j), (1+0j), (1+0j),

		(1+0j), (1+0j), (1+0j), (-1+0j), (1+0j), (1+0j), (-1+0j), (-1+0j),
		(-1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (1+0j),
		(-1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (-1+0j), (-1+0j), (1+0j),
		(1+0j), (1+0j), (-1+0j), (1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j))

        # Manual verification:
        # PREAMBLE: 
        # ( 1+0j), (-1+0j), (-1+0j), ( 1+0j), 
        # HEADER  : Bits 0-11: payload length in symbols (take care of order! LSB more to the 'left'!), bits 12-23: packet number, bits 24-31 8-BIT CRC
        # 
		# (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (-1+0j), (1+0j), (1+0j),
		# (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), 
		# (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j),
		# (-1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (1+0j), (1+0j), (1+0j)

        # which is 00000100 0000|0000 00000000|11111000 (packet length of 32 symbols)
        #
        # PAYLOAD : 
		# (1+0j), (1+0j), (1+0j), (-1+0j), (1+0j), (1+0j), (-1+0j), (-1+0j),
		# (-1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (1+0j),
		# (-1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (-1+0j), (-1+0j), (1+0j),
		# (1+0j), (1+0j), (-1+0j), (1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j))
        # which is 00010011 11111110 10000110 00101111
        # so each byte is reversed because its read LSB first, which is correct


        src = blocks.vector_source_b (src_data, repeat=False)
        packet_len = len(src_data)
        tagger = blocks.stream_to_tagged_stream(1, 1, packet_len, "packet_len")
        repacker = blocks.repack_bits_bb(8, 1, "packet_len", False, gr.GR_LSB_FIRST)
        
        #arguments: preamble, constel_header, constel_payload, header_formatter, lengthtagname, zero_padding, whiten, itemsize
        penc = packetizer.packet_encoder (preamble, constel_header, constel_payload, header_formatter, "packet_len",0, False,1 )
        snk = blocks.vector_sink_c(1)

        self.tb.connect (src, tagger)
        self.tb.connect (tagger, repacker)
        self.tb.connect (repacker, penc)
        self.tb.connect (penc, snk)
        self.tb.run ()
        result_data = snk.data ()
        #print "\n RESULT DATA",result_data,"\n"
        
    	self.assertFloatTuplesAlmostEqual (expected_result, result_data)   


    def test_packet_encoder_qpsk (self):
        preamble = (1,-1,-1,1)
        src_data = (0b11001000,0b01111111,0b01100001,0b11110100)

        
        constel_header   = digital.constellation_calcdist(([1,-1]), ([0, 1]), 2, 1).base()
        constel_payload = digital.constellation_calcdist(([-1-1j, 1-1j, -1+1j, 1+1j]), ([0, 1, 2, 3]), 4, 1).base() #00 to -1-j, 01 to 1-j, 10 to -1+j, 11 to 1+j
        
        header_formatter = digital.packet_header_default(32/constel_header.bits_per_symbol(), "packet_len", "packet_num", constel_header.bits_per_symbol())
        
        expected_result = preamble + \
         ((1+0j), (1+0j), (1+0j), (1+0j), (-1+0j), (1+0j), (1+0j), (1+0j),
  			(1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j),
   			(1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j),
    		(1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), 


		    (-0.707-0.707j), (0.707-0.707j), (-0.707-0.707j), (0.707+0.707j),
		    (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), (-0.707+0.707j), 
		    (-0.707+0.707j), (-0.707-0.707j), (0.707-0.707j), (-0.707+0.707j), 
		    (-0.707-0.707j), (-0.707+0.707j), (0.707+0.707j), (0.707+0.707j)) 

        # Manual verification:
        # PREAMBLE: 
        # ( 1+0j), (-1+0j), (-1+0j), ( 1+0j), 
        # HEADER  : Bits 0-11: payload length in symbols (take care of order! LSB more to the 'left'!), bits 12-23: packet number, bits 24-31 8-BIT CRC
        # 
		# 
		# (1+0j), (1+0j), (1+0j), (1+0j), (-1+0j), (1+0j), (1+0j), (1+0j),
		# (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j),
		# (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j),
		# (1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), 


        # which is 00001000 0000|0000 00000000|01101101 (packet length of 32 symbols)
        #
        # PAYLOAD : 
	    # (-0.707-0.707j), (0.707-0.707j), (-0.707-0.707j), (0.707+0.707j),
	    # (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), (-0.707+0.707j), 
	    # (-0.707+0.707j), (-0.707-0.707j), (0.707-0.707j), (-0.707+0.707j), 
	    # (-0.707-0.707j), (-0.707+0.707j), (0.707+0.707j), (0.707+0.707j)) 
        # which is 00 01 00 11  | 11 11 11 10 | 10 00 01 10 | 00 10 11 11
        # so each byte is reversed because its reading LSB first, which is correct


        src = blocks.vector_source_b (src_data, repeat=False)
        packet_len = len(src_data)
        tagger = blocks.stream_to_tagged_stream(1, 1, packet_len, "packet_len")
        repacker = blocks.repack_bits_bb(8, 1, "packet_len", False, gr.GR_LSB_FIRST)
        
        #arguments: preamble, constel_header, constel_payload, header_formatter, lengthtagname, zero_padding, whiten, itemsize
        penc = packetizer.packet_encoder (preamble, constel_header, constel_payload, header_formatter, "packet_len",0, False,1 )
        snk = blocks.vector_sink_c(1)

        self.tb.connect (src, tagger)
        self.tb.connect (tagger, repacker)
        self.tb.connect (repacker, penc)
        self.tb.connect (penc, snk)
        self.tb.run ()
        result_data = snk.data ()
        #print "\n RESULT DATA",result_data,"\n"
        
    	self.assertFloatTuplesAlmostEqual (expected_result, result_data,3)

    def test_packet_encoder_qpsk2 (self):
        preamble = (1,-1,-1,1)
        src_data = (0,0,0,1,0,0,1,1,
        			1,1,1,1,1,1,1,0,
        			1,0,0,0,0,1,1,0,
        			0,0,1,0,1,1,1,1)

        
        constel_header   = digital.constellation_calcdist(([1,-1]), ([0, 1]), 2, 1).base()
        constel_payload = digital.constellation_calcdist(([-1-1j, 1-1j, -1+1j, 1+1j]), ([0, 1, 2, 3]), 4, 1).base() #00 to -1-j, 01 to 1-j, 10 to -1+j, 11 to 1+j
        
        header_formatter = digital.packet_header_default(32/constel_header.bits_per_symbol(), "packet_len", "packet_num", constel_header.bits_per_symbol())
        
        expected_result = preamble + \
         ((1+0j), (1+0j), (1+0j), (1+0j), (-1+0j), (1+0j), (1+0j), (1+0j),
  			(1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j),
   			(1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j),
    		(1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), 


		    (-0.707-0.707j), (0.707-0.707j), (-0.707-0.707j), (0.707+0.707j),
		    (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), (-0.707+0.707j), 
		    (-0.707+0.707j), (-0.707-0.707j), (0.707-0.707j), (-0.707+0.707j), 
		    (-0.707-0.707j), (-0.707+0.707j), (0.707+0.707j), (0.707+0.707j)) 

        # Manual verification:
        # PREAMBLE: 
        # ( 1+0j), (-1+0j), (-1+0j), ( 1+0j), 
        # HEADER  : Bits 0-11: payload length in symbols (take care of order! LSB more to the 'left'!), bits 12-23: packet number, bits 24-31 8-BIT CRC
        # 
		# 
		# (1+0j), (1+0j), (1+0j), (1+0j), (-1+0j), (1+0j), (1+0j), (1+0j),
		# (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j),
		# (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j), (1+0j),
		# (1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), (-1+0j), (1+0j), (-1+0j), 


        # which is 00001000 0000|0000 00000000|01101101 (packet length of 32 symbols)
        #
        # PAYLOAD : 
	    # (-0.707-0.707j), (0.707-0.707j), (-0.707-0.707j), (0.707+0.707j),
	    # (0.707+0.707j), (0.707+0.707j), (0.707+0.707j), (-0.707+0.707j), 
	    # (-0.707+0.707j), (-0.707-0.707j), (0.707-0.707j), (-0.707+0.707j), 
	    # (-0.707-0.707j), (-0.707+0.707j), (0.707+0.707j), (0.707+0.707j)) 
        # which is 00 01 00 11  | 11 11 11 10 | 10 00 01 10 | 00 10 11 11
        # so each byte is reversed because its reading LSB first, which is correct


        src = blocks.vector_source_b (src_data, repeat=False)
        packet_len = len(src_data)
        tagger = blocks.stream_to_tagged_stream(1, 1, packet_len, "packet_len")
        #repacker = blocks.repack_bits_bb(8, 1, "packet_len", False, gr.GR_LSB_FIRST)
        
        #arguments: preamble, constel_header, constel_payload, header_formatter, lengthtagname, zero_padding, whiten, itemsize
        penc = packetizer.packet_encoder (preamble, constel_header, constel_payload, header_formatter, "packet_len",0, False,1 )
        snk = blocks.vector_sink_c(1)

        self.tb.connect (src, tagger)
        self.tb.connect (tagger, penc)
        self.tb.connect (penc, snk)
        self.tb.run ()
        result_data = snk.data ()
        #print "\n RESULT DATA",result_data,"\n"
        
    	self.assertFloatTuplesAlmostEqual (expected_result, result_data,3)   
if __name__ == '__main__':
    gr_unittest.run(qa_packet_encoder, "qa_packet_encoder.xml")
