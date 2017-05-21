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
    packetizr_packet_encoder.xml
    packetizr_packet_decoder.xml
    packetizr_modulate_vector.xml
    packetizr_tagged_stream_demux.xml
    packetizr_preamble_header_payload_demux.xml
    packetizr_tagged_whitener.xml
    packetizr_corr_est_cc.xml DESTINATION share/gnuradio/grc/blocks
)
