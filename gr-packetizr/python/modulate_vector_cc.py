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

def modulate_vector_cc(modulator, data):
    # vector_src = blocks.vector_source_f(data, repeat=False);
    # #filter::fir_filter_ccf::sptr filter = filter::fir_filter_ccf(1, taps);
    # vector_sink = blocks.vector_sink_c(1);

    # tb = gr.top_block("modulate_vector");

    # tb.connect(vector_src, 0, vector_sink, 0);
    # #tb.connect(modulator, 0, vector_sink, 0);
    # #tb.connect(filter, 0, vector_sink, 0);

    # tb.run();
    # #return (1,1,1)
    # return vector_sink.data();

    tb = gr.top_block ()

    src = blocks.vector_source_c (data, repeat=False)
    snk = blocks.vector_sink_c(1)

    tb.connect (src, modulator)
    tb.connect (modulator,snk)

    tb.run ()
    result_data = snk.data ()
    print "\n MODULATED DATA",result_data,"\n"
    return result_data
   