#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 Thomas Verelst.
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
import pmt
from gnuradio import gr
from gnuradio import digital
from gnuradio import blocks

"""
Applies the given pulse shaper filter (\param pulseshaper) on the given data (\param data).
"""
def pulseshape_vector(pulseshaper, data):

    tb = gr.top_block ("pulseshape_vector")

    src = blocks.vector_source_c (data, repeat=False)
    snk = blocks.vector_sink_c(1)

    tb.connect (src, pulseshaper)
    tb.connect (pulseshaper, snk)

    tb.run ()
    result_data = snk.data ()

    #print "\n MODULATED DATA",result_data,"\n"
    return result_data
   