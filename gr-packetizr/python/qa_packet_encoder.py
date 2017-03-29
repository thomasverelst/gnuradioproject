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
import packetizr_swig as packetizr

class qa_packet_encoder (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_packet_encoder_1 (self):
        preamble = (1,-1,-1,1)
        #preamble = tuple();
        packet_len = 4
        src_data = (200,127,97,244)

        header_formatter = digital.packet_header_default(4, "packet_len", "packet_num", 8)
        # constel_preamble = digital.constellation_calcdist(([-1-1j, -1+1j, 1+1j, 1-1j]), ([0, 1, 3, 2]), 4, 1).base()
        # constel_header = digital.constellation_calcdist(([-1-1j, -1+1j, 1+1j, 1-1j]), ([0, 1, 3, 2]), 4, 1).base()
        # constel_payload = digital.constellation_calcdist(([-1-1j, -1+1j, 1+1j, 1-1j]), ([0, 1, 3, 2]), 4, 1).base()
        constel_preamble = digital.constellation_calcdist(([1,-1]), ([0, 1]), 2, 1).base()
        constel_header = digital.constellation_calcdist(([1,-1]), ([0, 1]), 2, 1).base()
        constel_payload = digital.constellation_calcdist(([1,-1]), ([0, 1]), 2, 1).base()
        

        src_data = (200,127,97,244)
        
        expected_result = preamble + ()

        #
        # PREAMBLE: ( 1+0j), (-1+0j), (-1+0j), ( 1+0j), 
        # HEADER  : ( 1+0j), ( 1+0j), (-1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), 
        #           ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j),
        # which is 00100000|00000000|00000000|00000000 (packet length of 4)
        #
        # PAYLOAD : ( 1+0j), ( 1+0j), ( 1+0j), (-1+0j), ( 1+0j), ( 1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j), ( 1+0j), 
        #           (-1+0j), ( 1+0j), ( 1+0j), ( 1+0j), ( 1+0j), (-1+0j), (-1+0j), ( 1+0j), ( 1+0j), ( 1+0j), (-1+0j), ( 1+0j), (-1+0j), (-1+0j), (-1+0j), (-1+0j))
        # which is 00010011|11111110|10000110|00101111

        # because 200 = 11001000
        #         127 = 01111111
        #         97  = 01100001
        #         244 = 11110100
        #reversed!


        src = blocks.vector_source_b (src_data, repeat=False)
        tagger = blocks.stream_to_tagged_stream(1, 1, packet_len, "packet_len")
        penc = packetizr.packet_encoder (preamble, constel_header, constel_payload, header_formatter, "packet_len",1) #itemsize is in bytes

        snk = blocks.vector_sink_c(1)
        #self.tb.connect (src, unpack0)
        self.tb.connect (src, tagger)
        self.tb.connect (tagger, penc)
        self.tb.connect (penc, snk)
        self.tb.run ()
        result_data = snk.data ()
        print "\n RESULT DATA",result_data,"\n"
        
        #self.assertFloatTuplesAlmostEqual (expected_result, result_data, 6)   
    def test_packet_encoder_2 (self):
        preamble = (1,-1,-1,1)
        #preamble = tuple();
        packet_len = 2
        src_data = (200,127,97,244)

        header_formatter = digital.packet_header_default(4, "packet_len", "packet_num", 8)
        constel_preamble = digital.constellation_bpsk().base()
        constel_header = digital.constellation_qpsk().base() # QPSK: 00 maps to -1-j, 01 to -1+j, 10 to 1-j, 11 to 1+j
        constel_payload = digital.constellation_qpsk().base()
        
        # constel_preamble = digital.constellation_calcdist(([-1-1j, -1+1j, 1+1j, 1-1j]), ([3, 2, 1, 0]), 4, 1).base()
        # constel_header = digital.constellation_calcdist(([-1-1j, -1+1j, 1+1j, 1-1j]), ([3, 2, 1, 0]), 4, 1).base()
        # constel_payload = digital.constellation_calcdist(([-1-1j, -1+1j, 1+1j, 1-1j]), ([3, 2, 1, 0]), 4, 1).base()
        # constel_preamble = digital.constellation_calcdist(([1,-1]), ([0, 1]), 2, 1).base()
        # constel_header = digital.constellation_calcdist(([1,-1]), ([0, 1]), 2, 1).base()
        #constel_payload = digital.constellation_calcdist(([1,-1]), ([1, 0]), 2, 1).base()
        

        src_data = (200,127,97,244)
        
        expected_result = preamble + ()

        #
        # PREAMBLE: ( 1+0j), (-1+0j), (-1+0j), ( 1+0j), 
        # HEADER  : (-0.707+0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), 
         #          (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j),
        # which is 01000000|00000000|00000000|00000000 (packet length of 4)
        # which is 1 0 0 0 | .....
        #
        # PAYLOAD :  (-0.707-0.707j), (-0.707+0.707j), (-0.707-0.707j), (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), (0.707+0.707j)
        #             0                 1               0               2               2               2               2               3
        # which is 00,01,00,11|11,11,11,10|10,00,01,10|00,10,11,11
        # which is 0  1  0  3 |3  3  3  2 |2  0  1  1 |0  2  3  3

        # because 200 = 11001000
        #         127 = 01111111
        #         97  = 01100001
        #         244 = 11110100
        #reversed, which is good!



        #QPSK RESULT DATA (-0.707+0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707+0.707j), (-0.707-0.707j), (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), (0.707-0.707j), (0.707+0.707j), (1+0j), (-1+0j), (-1+0j), (1+0j), (-0.707+0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (0.707+0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (-0.707-0.707j), (0.707+0.707j), (-0.707-0.707j), (-0.707+0.707j), (0.707+0.707j), (-0.707-0.707j), (0.707+0.707j), (0.707-0.707j), (0.707-0.707j)) 


        src = blocks.vector_source_b (src_data, repeat=False)
        tagger = blocks.stream_to_tagged_stream(1, 1, packet_len, "packet_len")
        penc = packetizr.packet_encoder (preamble, constel_header, constel_payload,  header_formatter, "packet_len", 1) #itemsize is in bytes

        snk = blocks.vector_sink_c(1)
        #self.tb.connect (src, unpack0)
        self.tb.connect (src, tagger)
        self.tb.connect (tagger, penc)
        self.tb.connect (penc, snk)
        self.tb.run ()
        result_data = snk.data ()
        print "\n QPSK RESULT DATA",(result_data),"\n"
        
        #self.assertFloatTuplesAlmostEqual (expected_result, result_data, 6)   

if __name__ == '__main__':
    gr_unittest.run(qa_packet_encoder, "qa_packet_encoder.xml")
