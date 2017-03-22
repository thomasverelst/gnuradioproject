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

#ifndef INCLUDED_PACKETIZER_PACKET_ENCODER_BC_IMPL_H
#define INCLUDED_PACKETIZER_PACKET_ENCODER_BC_IMPL_H

#include <packetizer/packet_encoder_bc.h>

namespace gr {
  namespace packetizer {

    class packet_encoder_bc_impl : public packet_encoder_bc
    {
     private:
      // Nothing to declare in this block.

     protected:
      int calculate_output_stream_length(const gr_vector_int &ninput_items);

     public:
      packet_encoder_bc_impl(int sps,int  header_constel,int  payload_constel, int preamble, char* length_tag_key);
      ~packet_encoder_bc_impl();

      // Where all the action really happens
      int work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace packetizer
} // namespace gr

#endif /* INCLUDED_PACKETIZER_PACKET_ENCODER_BC_IMPL_H */

