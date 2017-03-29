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
import packetizr_swig as packetizr

class qa_tagged_stream_demux_xx (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_tagged_stream_demux (self):
    	packet_len = 7

        # set up fg
        src_data = (200,127,97,244, 23, 142, 55, 12)
        exp_res1 = (200,127,0)
        exp_res1 = (97,244,23)
        exp_res1 = (142,55,0)

        src = blocks.vector_source_b (src_data, repeat=False)
     
        tagger = blocks.stream_to_tagged_stream(1, 1, packet_len, "packet_len")
        demux = packetizr.tagged_stream_demux_xx(1,"packet_len", (2,3))

        snk1 = blocks.vector_sink_b(1)
        snk2 = blocks.vector_sink_b(1)
        snk3 = blocks.vector_sink_b(1)

        self.tb.connect (src, tagger)
        self.tb.connect (tagger, demux)
        self.tb.connect ((demux,0), (snk1, 0))
        self.tb.connect ((demux,1), (snk2, 0))
        self.tb.connect ((demux,2), (snk3, 0))
        self.tb.run ()
        res_data1 = snk1.data ()
        res_data2 = snk2.data ()
        res_data3 = snk3.data ()

        print "TAGGED STREAM DEMUX test 1; result 1",(res_data1),"\n"
        print "TAGGED STREAM DEMUX test 1; result 2",(res_data2),"\n"
        print "TAGGED STREAM DEMUX test 1; result 3",(res_data3),"\n"
        assertTupleEqual(res_data1, exp_res1)
        assertTupleEqual(res_data2, exp_res2)
        assertTupleEqual(res_data3, exp_res3)


if __name__ == '__main__':
    gr_unittest.run(qa_tagged_stream_demux_xx, "qa_tagged_stream_demux_xx.xml")
