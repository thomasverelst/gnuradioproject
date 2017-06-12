/* -*- c++ -*- */
/* 
 * Copyright 2017 Thomas Verelst.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_PACKETIZER_PACKET_ENCODER_IMPL_H
#define INCLUDED_PACKETIZER_PACKET_ENCODER_IMPL_H

#include <packetizer/packet_encoder.h>
#include <packetizer/whitener.h>
#include <gnuradio/digital/constellation.h>
#include <gnuradio/digital/packet_header_default.h>

namespace gr {
  namespace packetizer {

    class packet_encoder_impl : public packet_encoder
    {
    private:
      
      gr::digital::constellation_sptr d_constel_header;
      gr::digital::constellation_sptr d_constel_payload;
      std::vector<int> d_preamble;
      gr::digital::packet_header_default::sptr d_header_formatter;
      int d_zero_padding;
      bool d_whiten;
      size_t d_itemsize;
      kernel::whitener d_whitener;
      int d_last_diff;
      int d_last_diff_payload;
      bool d_diff_header;
      bool d_diff_payload;
      

     protected:
      int calculate_output_stream_length(const gr_vector_int &ninput_items);

     public:

      packet_encoder_impl(
        const std::vector<int> preamble, 
        const digital::constellation_sptr constel_header, 
        const digital::constellation_sptr constel_payload, 
        const digital::packet_header_default::sptr &header_formatter, 
        const bool diff_header,
        const bool diff_payload,
        const std::string &lengthtagname, 
        const int zero_padding, 
        const bool whiten,
        const size_t itemsize
      );
      ~packet_encoder_impl();

      // Where all the action really happens
      int work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);

      const static unsigned char random_mask[4096];
    };

  } // namespace packetizer
} // namespace gr

#endif /* INCLUDED_PACKETIZER_PACKET_ENCODER_IMPL_H */

