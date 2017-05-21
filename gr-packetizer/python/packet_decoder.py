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
import packetizer

class packet_decoder(gr.hier_block2):
    """
    docstring for block packet_decoder
    """
    def __init__(self, preamble, constel_header, constel_payload, header_formatter, triggertagname, do_costas, soft_output, do_whiten, samp_rate, itemsize):
        gr.hier_block2.__init__(self,
            "packet_decoder",
            gr.io_signature(1, 1, gr.sizeof_gr_complex),  # Input signature
            gr.io_signature(1, 1, gr.sizeof_float if soft_output else gr.sizeof_char))    # Output signature
        self.message_port_register_hier_out("header_data")

        #Demux
        header_payload_demux = packetizer.preamble_header_payload_demux(header_formatter.header_len(), 1, 0, "packet_len", triggertagname, True, gr.sizeof_gr_complex, "rx_time", samp_rate, ("phase_est", "time_est"), 0, len(preamble))

        # Feedback loop for payload length
        if(do_costas):
            header_costas = digital.costas_loop_cc(3.14*2/1000, 2**constel_header.bits_per_symbol(), False)
        #header_repack_bits = blocks.repack_bits_bb(constel_header.bits_per_symbol(), 1, "", False, gr.GR_LSB_FIRST)
        header_constel_decoder = digital.constellation_decoder_cb(constel_header)
        header_headerparser = digital.packet_headerparser_b(header_formatter.base())

        # Output
        if(do_costas):
            payload_costas = digital.costas_loop_cc(3.14*2/1000, 2**constel_payload.bits_per_symbol(), False)
        

        if(do_whiten):
            payload_tagged_whitener = packetizer.tagged_whitener(False, (), 1, "packet_len")

        if(soft_output):
            payload_constel_soft_decoder = digital.constellation_soft_decoder_cf(constel_payload.base())
        else:
            payload_constel_decoder = digital.constellation_decoder_cb(constel_payload)
            #payload_repack_symbols = blocks.repack_bits_bb(8,8, "", False, gr.GR_LSB_FIRST)
            payload_repack_bits = blocks.repack_bits_bb(constel_payload.bits_per_symbol(), 1, "packet_len", False, gr.GR_MSB_FIRST)
        #Connect

        #Input
        self.connect(self, (header_payload_demux, 0))
        
        #Header chain
        if(do_costas):
            self.connect((header_payload_demux, 0), header_costas)
            self.connect(header_costas, header_constel_decoder)
        else:
            self.connect((header_payload_demux, 0), header_constel_decoder)
        self.connect(header_constel_decoder, header_headerparser)
        self.msg_connect((header_headerparser, "header_data"), (header_payload_demux, "header_data"))
        self.msg_connect((header_headerparser, "header_data"), (self, "header_data"))

        #Payload chain
        
        if(soft_output):
            if(do_costas):
                self.connect((header_payload_demux, 1), payload_costas)
                self.connect(payload_costas, payload_constel_soft_decoder)
            else:
                self.connect((header_payload_demux, 1), payload_constel_soft_decoder) 
            
            self.connect(payload_constel_soft_decoder, self)

        else:
            if(do_costas):
                self.connect((header_payload_demux, 1), payload_costas)
                self.connect(payload_costas, payload_constel_decoder)
            else:
                self.connect((header_payload_demux, 1), payload_constel_decoder)        


            self.connect(payload_constel_decoder, payload_repack_bits)
            #self.connect(payload_repack_symbols, payload_repack_bits)

            if(do_whiten):
                self.connect(payload_repack_bits, payload_tagged_whitener)
                self.connect(payload_tagged_whitener, self)
            else:
                self.connect(payload_repack_bits, self)
