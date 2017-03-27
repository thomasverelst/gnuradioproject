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

import pmt
from gnuradio import gr
from gnuradio import digital
from gnuradio import blocks

class packet_decoder(gr.hier_block2):
    """
    docstring for block packet_decoder
    """
    def __init__(self, preamble, constel_header, constel_payload, header_formatter, lengthtagname, tag_pos, samp_rate, itemsize):
        gr.hier_block2.__init__(self,
            "packet_decoder",
            gr.io_signature(1, 1, gr.sizeof_gr_complex),  # Input signature
            gr.io_signature(1, 1, gr.sizeof_char))    # Output signature

        #Demux
        header_payload_demux = digital.header_payload_demux(header_formatter.header_len()*8/constel_header.bits_per_symbol(), 1, 0, "packet_len", "packet_len", True, 
            gr.sizeof_gr_complex, "", samp_rate,()
        )

        # Feedback loop for payload length
        repack_header_bits = blocks.repack_bits_bb(constel_header.bits_per_symbol(), 8, "", False, gr.GR_LSB_FIRST)
        constel_decoder_header = digital.constellation_decoder_cb(constel_header)
        headerparser = digital.packet_headerparser_b(header_formatter.base())

        # Output
        constel_decoder_payload = digital.constellation_decoder_cb(constel_payload)

        #Connect
        self.connect(self, (header_payload_demux, 0))
        

        self.connect((header_payload_demux, 0), constel_decoder_header)
        self.connect(constel_decoder_header, repack_header_bits)
        self.connect(repack_header_bits, headerparser)
        self.msg_connect((headerparser, "header_data"), (header_payload_demux, "header_data"))

        self.connect((header_payload_demux, 1), constel_decoder_payload)
        self.connect(constel_decoder_payload, self)
