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
#include "packet_encoder_impl.h"
#include <stdio.h>
#include <iostream>
using namespace std;

namespace gr {
  namespace packetizr {

    packet_encoder::sptr
    packet_encoder::make(unsigned int sps, int preamble, unsigned int header_constel, unsigned int payload_constel, size_t itemsize, const std::string &lengthtagname)
    {
      return gnuradio::get_initial_sptr
        (new packet_encoder_impl(sps, preamble, header_constel, payload_constel, itemsize, lengthtagname));
    }

    /*
     * The private constructor
     */
    packet_encoder_impl::packet_encoder_impl(unsigned int sps, int preamble, unsigned int header_constel, unsigned int payload_constel, size_t itemsize, const std::string &lengthtagname)
      : gr::tagged_stream_block("packet_encoder",
              gr::io_signature::make(2, 2, itemsize), // sizeof(char)
              gr::io_signature::make(1, 1, itemsize), lengthtagname),
      d_itemsize(itemsize)
    {
       set_tag_propagation_policy(TPP_DONT);
    }

    /*
     * Our virtual destructor.
     */
    packet_encoder_impl::~packet_encoder_impl()
    {
    }

    int
    packet_encoder_impl::calculate_output_stream_length(const gr_vector_int &ninput_items)
    {
      int nout = 0;
      for (unsigned i = 0; i < ninput_items.size(); i++) {
        nout += ninput_items[i];
      }
      return nout;
    }

    int
    packet_encoder_impl::work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      unsigned char *out = (unsigned char *) output_items[0];
      int n_produced = 0;

      set_relative_rate(ninput_items.size());

      cout << "$$ NUMBER OF INPUTS:" << ninput_items.size() << "\n";
      // for each input 
      for (unsigned int i = 0; i < input_items.size(); i++) {

        // Get array of all input items for this input
        const unsigned char *in = (const unsigned char *) input_items[i];

        cout << "$$ START printing in for input "<< i << "do";
        for (unsigned int j = 0; j < ninput_items[j]; j++) {
          cout << j;
        }
        cout << "END \n";

        // Get tags in this input item stream
        std::vector<tag_t> tags;
        get_tags_in_range(tags, i, nitems_read(i), nitems_read(i)+ninput_items[i]);

        cout << "$$ NUMBER OF TAGS" << tags.size() << "\n";
        // for each tag
        for (unsigned int j = 0; j < tags.size(); j++) {
          uint64_t offset = tags[j].offset - nitems_read(i) + nitems_written(0) + n_produced;
          // if (i =é= d_tag_preserve_head_pos && tags[j].offset == nitems_read(i)) {
          //   offset -= n_produced;
          // }

          // Add tag to output stream at right offset
          cout << "TAG KEY" << tags[j].key << "\n";
          cout << "TAG VALUE" << tags[j].value << "\n";
          add_item_tag(0, offset, tags[j].key, tags[j].value);
        }
        
        // put sequentially in memory
        memcpy((void *) out, (const void *) in, ninput_items[i] * d_itemsize);
        out += ninput_items[i] * d_itemsize; // Update pointer
        n_produced += ninput_items[i]; // Update produced amount of items
      }

      return n_produced;
    }

  } /* namespace packetizr */
} /* namespace gr */

