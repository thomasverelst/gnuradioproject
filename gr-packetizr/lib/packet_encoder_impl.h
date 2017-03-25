/* -*- c++ -*- */
/* 
 * Copyright 2017 <+YOU OR YOUR COMPANY+>.
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

#ifndef INCLUDED_PACKETIZR_PACKET_ENCODER_IMPL_H
#define INCLUDED_PACKETIZR_PACKET_ENCODER_IMPL_H

#include <packetizr/packet_encoder.h>
#include <gnuradio/digital/constellation.h>
#include <gnuradio/digital/packet_header_default.h>
#include <gnuradio/filter/firdes.h>
#include <gnuradio/filter/pfb_arb_resampler.h>

namespace gr {
  namespace packetizr {

    class packet_encoder_impl : public packet_encoder
    {
    private:
      
      gr::digital::constellation_sptr d_constel_preamble;
      gr::digital::constellation_sptr d_constel_header;
      gr::digital::constellation_sptr d_constel_payload;
      std::vector<int> d_preamble;
      gr::digital::packet_header_default::sptr d_header_formatter;
      size_t d_itemsize;

     protected:
      int calculate_output_stream_length(const gr_vector_int &ninput_items);

     public:
      packet_encoder_impl(const std::vector<int> preamble, digital::constellation_sptr constel_preamble, digital::constellation_sptr constel_header, digital::constellation_sptr  constel_payload, size_t itemsize, const digital::packet_header_default::sptr &header_formatter, const std::string &lengthtagname);
      ~packet_encoder_impl();

      // Where all the action really happens
      int work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace packetizr
} // namespace gr

#endif /* INCLUDED_PACKETIZR_PACKET_ENCODER_IMPL_H */

