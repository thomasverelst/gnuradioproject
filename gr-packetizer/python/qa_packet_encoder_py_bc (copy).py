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
from packet_encoder_py_bc import packet_encoder_py_bc

class qa_packet_encoder_py_bc (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        header_formatter = digital.packet_header_default(8, "packet_len", "packet_num", 1)

    	src_data = (0, 1, 8, 4, 3)
    	expected_result = (0, 2, -4, 11, -1)
    	src = blocks.vector_source_b (src_data, repeat=False)
    	tagger = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 4, "packet_len")
        header_gen = digital.packet_headergenerator_bb(header_formatter, "packet_len")
    	penc = packet_encoder_py_bc (1, None, None, (0,1,0,1,1,0), "len")

    	snk = blocks.vector_sink_f ()
    	self.tb.connect (src, tagger)
    	self.tb.connect (tagger, header_gen)
        self.tb.connect (header_gen, (penc, 0))
        self.tb.connect (tagger, (penc, 1))
    	self.tb.connect (penc, snk)
    	self.tb.run ()
    	result_data = snk.data ()
        print result_data
    	self.assertFloatTuplesAlmostEqual (expected_result, result_data, 6)   


if __name__ == '__main__':
    gr_unittest.run(qa_packet_encoder_py_bc, "qa_packet_encoder_py_bc.xml")
