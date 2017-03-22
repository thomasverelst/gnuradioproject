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

import numpy
from gnuradio import gr

class packet_encoder_py_bc(gr.basic_block):
    """
    docstring for block packet_encoder_py_bc
    """
    def __init__(self, sps, header_constel, payload_constel, preamble, length_tag_key):
        gr.basic_block.__init__(self,
            name="packet_encoder_py_bc",
            in_sig=[numpy.uint8,numpy.uint8],
            out_sig=[numpy.float32])

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):
       # print "inputitems", input_items[0]
        #print "outputitems", output_items[0]
        output_items[0][:] = numpy.float32(input_items[0][:4])
        # output_items[0][:] = input_items[0] + input_items[1]
 
        #consume(0, len(input_items[0]))
        #print "outputitems", output_items[0]
        #self.consume_each(len(input_items[0]))
        return len(output_items[0])
        # in0 = input_items[0]
        # out = output_items[0]
        # # <+signal processing here+>
        # out[:] = in0
        # return len(output_items[0])
