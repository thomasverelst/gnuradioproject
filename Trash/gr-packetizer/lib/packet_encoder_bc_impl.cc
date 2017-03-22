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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "packet_encoder_bc_impl.h"

namespace gr {
  namespace packetizer {

    packet_encoder_bc::sptr
    packet_encoder_bc::make(int sps, int header_constel,int payload_constel, int preamble, char* length_tag_key)
    {
      return gnuradio::get_initial_sptr
        (new packet_encoder_bc_impl(sps, header_constel,payload_constel, preamble, length_tag_key));
    }

    /*
     * The private constructor
     */
    packet_encoder_bc_impl::packet_encoder_bc_impl(int sps, int header_constel,int payload_constel, int preamble, char* length_tag_key)
      : gr::tagged_stream_block("packet_encoder_bc",
              gr::io_signature::make(2, 2, sizeof(sizeof(char))),
              gr::io_signature::make(1, 1, sizeof(sizeof(gr_complex))), length_tag_key)
    {}

    /*
     * Our virtual destructor.
     */
    packet_encoder_bc_impl::~packet_encoder_bc_impl()
    {
    }

    int
    packet_encoder_bc_impl::calculate_output_stream_length(const gr_vector_int &ninput_items)
    {
      int noutput_items = ninput_items[0]/* <+set this+> */;
      return noutput_items ;
    }

    int
    packet_encoder_bc_impl::work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const unsigned char *in = (const unsigned char *) input_items[0];
      gr_complex *out = (gr_complex*) output_items[0];

      for(int i = 0; i<noutput_items; i++){
        out[i] = in[i];
      }
      // Do <+signal processing+>
      consume_each(noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace packetizer */
} /* namespace gr */

