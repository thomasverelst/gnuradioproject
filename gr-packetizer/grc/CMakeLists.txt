# Copyright 2011 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

install(FILES
    packetizer_preamble_header_payload_demux.xml
    packetizer_tagged_whitener.xml
    packetizer_packet_encoder.xml
    packetizer_packet_decoder.xml
    packetizer_pulseshape_vector.xml
    packetizer_corr_est_cc.xml
    packetizer_message_sequence_checker.xml
    packetizer_tagged_stream_fix.xml DESTINATION share/gnuradio/grc/blocks
)
