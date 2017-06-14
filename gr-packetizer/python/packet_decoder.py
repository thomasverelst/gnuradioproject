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
import numpy
import packetizer

class packet_decoder(gr.hier_block2):
    """
    Decodes packets which have been generated with the packet encoder. (format: preamble/header/payload)
    Will output payload symbols (soft or hard output) and header data on the message port. 

    \param preamble Sequence of modulated preamble symbols (BPSK: -1 and 1)
    \param constel_header Constellation object for header
    \param constel_payload Constellation object for payload
    \param header_formatter Header formatter object
    \param samp_rate Sample rate (optional for time tag)
    \param diff_header Boolean indicating to use differential decoding for header
    \param diff_payload Boolean indicating to use differential decoding for payload
    \param triggertagname Name of tag that indicates the start of the packet (often set by frame sync)
    \param do_costas Indicate whether to use Costas Loop for phase sync/carrier tracking
    \param soft_output Use soft output (floats) or hard output (unpacked bytes with 1 bit/symbol)
    \param do_whiten Indicate whether to dewhiten packet data (if whitened with packet encoder)
    \param itemsize No effect yet. Input is always complex samples, output is always floats (for soft output) or unpacked bytes (1bit/symbol).
    """
    def __init__(self, preamble, constel_header, constel_payload, header_formatter, samp_rate=32000,  diff_header=False, diff_payload=False,triggertagname="corr_est", do_costas=False, soft_output=False, do_whiten=False, itemsize=1):
        gr.hier_block2.__init__(self,
            "packet_decoder",
            gr.io_signature(1, 1, gr.sizeof_gr_complex),  # Input signature
            gr.io_signature(1, 1, gr.sizeof_float if soft_output else gr.sizeof_char))    # Output signature
        self.message_port_register_hier_out("header_data")

        if(soft_output == True and diff_payload == True):
            print "WARNING: Packet Decoder: soft output with differential decoding of payload not supported! Soft output disabled"
            soft_output = False

        #Demux
        header_payload_demux = packetizer.preamble_header_payload_demux(header_formatter.header_len(), 1, 0, "packet_len", triggertagname, True, gr.sizeof_gr_complex, "rx_time", samp_rate, ("phase_est", "time_est"), 0, len(preamble), constel_payload.bits_per_symbol())

        # Feedback loop for payload length
        if(do_costas):
            header_costas = digital.costas_loop_cc(3.14*2/100, 2**constel_header.bits_per_symbol(), False)

        if(diff_header):
            header_diff_dec = digital.diff_decoder_bb(len(constel_header.points()))

        #header_repack_bits = blocks.repack_bits_bb(constel_header.bits_per_symbol(), 1, "", False, gr.GR_LSB_FIRST)
        header_constel_decoder = digital.constellation_decoder_cb(constel_header)
        header_headerparser = digital.packet_headerparser_b(header_formatter.base())

        # Output
        if(do_costas):
            payload_costas = digital.costas_loop_cc(3.14*2/100, 2**constel_payload.bits_per_symbol(), False)
        
        
        

        if soft_output:
            payload_constel_decoder = digital.constellation_soft_decoder_cf(constel_payload.base())
            payload_tagged_stream_fix = packetizer.tagged_stream_fix("packet_len", numpy.float32)
        else:
            payload_constel_decoder = digital.constellation_decoder_cb(constel_payload.base())
            payload_tagged_stream_fix = packetizer.tagged_stream_fix("packet_len", numpy.int8)
            if(diff_payload):
                payload_diff_dec = digital.diff_decoder_bb(len(constel_payload.points()))
            payload_repack_bits = blocks.repack_bits_bb(constel_payload.bits_per_symbol(), 1, "", False, gr.GR_MSB_FIRST)
            payload_repack_bits_2 = blocks.repack_bits_bb(1, constel_payload.bits_per_symbol(), "", False, gr.GR_MSB_FIRST)
            payload_repack_bits_3 = blocks.repack_bits_bb(constel_payload.bits_per_symbol(), 1, "", False, gr.GR_MSB_FIRST)
            
            if(do_whiten):
                payload_tagged_whitener = packetizer.tagged_whitener(False, (), 1, "packet_len")
            #payload_slice_bits = digital.binary_slicer_fb()


       
        


        #Connect

        #Input
        self.connect(self, (header_payload_demux, 0))
        
        #Header chain
        if(do_costas):
            self.connect((header_payload_demux, 0), header_costas)
            self.connect(header_costas, header_constel_decoder)
        else:
            self.connect((header_payload_demux, 0), header_constel_decoder)

        
        if(diff_header):
            self.connect(header_constel_decoder, header_diff_dec)
            self.connect(header_diff_dec, header_headerparser)
        else:
            self.connect(header_constel_decoder, header_headerparser)

        self.msg_connect((header_headerparser, "header_data"), (header_payload_demux, "header_data"))
        self.msg_connect((header_headerparser, "header_data"), (self, "header_data"))


        #Payload chain
        if do_costas:
            self.connect((header_payload_demux, 1), payload_costas)
            self.connect(payload_costas, payload_constel_decoder)
        else:
            self.connect((header_payload_demux, 1), payload_constel_decoder) 
            
       
        if soft_output:
            self.connect(payload_constel_decoder, payload_tagged_stream_fix)
            self.connect(payload_tagged_stream_fix, self)

        else:
            self.connect(payload_constel_decoder, payload_repack_bits)
            self.connect(payload_repack_bits, payload_tagged_stream_fix)

            if(diff_payload):
                self.connect(payload_tagged_stream_fix, payload_repack_bits_2)
                self.connect(payload_repack_bits_2, payload_diff_dec)
                self.connect(payload_diff_dec, payload_repack_bits_3)
                if(do_whiten):
                    self.connect(payload_repack_bits_3, payload_tagged_whitener)
                    self.connect(payload_tagged_whitener, self)
                else:
                    self.connect(payload_repack_bits_3, self)
            else:
                if(do_whiten):
                    self.connect(payload_tagged_stream_fix, payload_tagged_whitener)
                    self.connect(payload_tagged_whitener, self)
                else:
                    self.connect(payload_tagged_stream_fix, self)
            