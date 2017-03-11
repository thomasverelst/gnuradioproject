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
#include <gnuradio/digital/constellation.h>
#include <gnuradio/filter/firdes.h>
#include "packet_encoder_impl.h"
#include <stdio.h>
#include <iostream>

using namespace std;

namespace gr {
  namespace packetizr {

    packet_encoder::sptr
    packet_encoder::make(unsigned int sps, int preamble, digital::constellation_sptr header_constel, digital::constellation_sptr  payload_constel, size_t itemsize, const std::string &lengthtagname)
    {
      return gnuradio::get_initial_sptr
        (new packet_encoder_impl(sps, preamble, header_constel, payload_constel, itemsize, lengthtagname));
    }

    /*
     * The private constructor
     */
    packet_encoder_impl::packet_encoder_impl(unsigned int sps, int preamble, digital::constellation_sptr header_constel, digital::constellation_sptr  payload_constel, size_t itemsize, const std::string &lengthtagname)
      : gr::tagged_stream_block("packet_encoder",
              gr::io_signature::make(2, 2, sizeof(char)), // sizeof(char)
              gr::io_signature::make(1, 1, sizeof(float)), lengthtagname),
        d_header_constel(header_constel),
        d_payload_constel(payload_constel),
        d_itemsize(1),
        d_sps(sps)
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
      nout += ninput_items[0] * 8 / d_header_constel->bits_per_symbol();
      nout += ninput_items[1] * 8 / d_payload_constel->bits_per_symbol();
      return nout;
    }

    void 
    unpack_bits(const unsigned char* packed, unsigned char *unpacked, unsigned int n, unsigned short bits_n){
      
      unsigned short newval = 0;
      unsigned short tempindex = 1;
      unsigned short newindex = 0;
      
      // for every incoming byte
      for(unsigned int i = 0; i < n; i++) {
        char val = packed[i];

        // for every bit of incoming byte
        for(unsigned int j = 0; j < 8; j++){ // TODO hardcoded char length
          newval = (newval << 1) | (val & 0b1);
          if(tempindex == bits_n){
              unpacked[newindex] = newval;
              newindex++;
              newval = 0;
              tempindex = 0;
          }
          tempindex++;
          val = val >> 1; 
        }
      }
    }

    int
    packet_encoder_impl::work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      
      unsigned int *out = (unsigned int *) output_items[0]; // set pointer where to put output data
      int n_produced = 0;

      // approximated input/output rate (assumes both input stream has same length, wrong!)
      // Needed for scheduling?
      set_relative_rate(ninput_items.size()); 



      /* Process header data */

      // Get array of all input items from header data input
      const unsigned char *header_in = (const unsigned char *) input_items[0];

      // Get tags in this input item stream
      std::vector<tag_t> tags;
      get_tags_in_range(tags, 0, nitems_read(0), nitems_read(0)+ninput_items[0]);

      for (unsigned int j = 0; j < tags.size(); j++) {
        uint64_t offset = tags[j].offset - nitems_read(0) + nitems_written(0) + n_produced;
      //       // if (i =é= d_tag_preserve_head_pos && tags[j].offset == nitems_read(i)) {
      //       //   offset -= n_produced;
      //       // }

        // Add tag to output stream at right offset
        add_item_tag(0, offset, tags[j].key, tags[j].value);
      }

      // Do mapping

      // TODO now assuming itemsize = 1
      cout << "HEADER : CONSTEL BITS PER SYMBOL" << d_header_constel->bits_per_symbol() << "\n";
      for (unsigned int j = 0; j < ninput_items[0]; j++) {
        cout << "VAL"<< (int *)header_in[j] <<"\n";
      }
          

      // put sequentially in memory
     // memcpy((void *) out, (const void *) header_in, ninput_items[0] * d_itemsize);
     // out += ninput_items[0] * d_itemsize; // Update pointer
     // n_produced += ninput_items[1]; // Update produced amount of items



      /* Process payload data */

      const unsigned char *payload_in = (const unsigned char *) input_items[1];

      // Get tags in this input item stream
      get_tags_in_range(tags, 1, nitems_read(1), nitems_read(1)+ninput_items[1]);

      for (unsigned int j = 0; j < tags.size(); j++) {
        uint64_t offset = tags[j].offset - nitems_read(1) + nitems_written(0) + n_produced;
      //       // if (i =é= d_tag_preserve_head_pos && tags[j].offset == nitems_read(i)) {
      //       //   offset -= n_produced;
      //       // }

        // Add tag to output stream at right offset
        add_item_tag(0, offset, tags[j].key, tags[j].value);
      }


      // TODO now assuming itemsize = 1
      cout << "PAYLOAD : CONSTEL BITS PER SYMBOL" << d_payload_constel->bits_per_symbol() << "\n";
      for (unsigned int j = 0; j < ninput_items[1]; j++) {
        cout << "VAL"<< (int *)payload_in[j] <<"\n";
      }

      // unpack bits in a char to multiple chars with k significant bit (LSB)
      // Where k is the number of bits per symbol for the given constellation
     unsigned int payload_bps = d_payload_constel->bits_per_symbol(); // TODO ccan be defined ouside work
     unsigned int payload_length = ninput_items[1]*8/payload_bps; // Payload length in bytes
     
     unsigned char *payload_unpacked = new unsigned char[payload_length];
     gr_complex *payload_symbols = new gr_complex[payload_length];
     float *tempout = new float[payload_length];
     unpack_bits(payload_in, payload_unpacked, ninput_items[1], payload_bps);
      

      //Do mapping
      cout << "PAYLOAD : MAPPING : CONSTEL BITS PER SYMBOL" << d_payload_constel->bits_per_symbol() << "\n";
      for (unsigned int j = 0; j < payload_length; j++) {
        unsigned int val = (unsigned int) payload_unpacked[j];
        d_payload_constel->map_to_points(val, &payload_symbols[j]);
        tempout[j] = real(payload_symbols[j]);
        cout << " value " << val << " mapped to constellation point " << tempout[j] << "\n";
      }

      // Modulate


      // nfilts = 32
      //   ntaps = nfilts * 11 * int(self._samples_per_symbol)    # make nfilts filters of ntaps each
      //   self.rrc_taps = filter.firdes.root_raised_cosine(
      //       nfilts,          # gain
      //       nfilts,          # sampling rate based on 32 filters in resampler
      //       1.0,             # symbol rate
      //       self._excess_bw, # excess bandwidth (roll-off factor)
      //       ntaps)
      //   self.rrc_filter = filter.pfb_arb_resampler_ccf(self._samples_per_symbol,
      //                                                  self.rrc_taps)

      // TODO should be defined outside of work function
      unsigned int nfilts = 32;
      unsigned int ntaps = nfilts * 11 * d_sps;
      std::vector<float> rrc_taps = gr::filter::firdes::root_raised_cosine(nfilts, nfilts, 1.0, 0.35,ntaps);
    

      // put sequentially in memory
      memcpy((void *) out, (const void *) tempout, payload_length);
      out += payload_length; // Update pointer
      n_produced += payload_length; // Update produced amount of items


      /* Return */
      return n_produced;
    }



    //   unsigned char *out = (unsigned char *) output_items[0];
    //   int n_produced = 0;

    //   set_relative_rate(ninput_items.size());

    //   cout << "$$ NUMBER OF INPUTS:" << ninput_items.size() << "\n";
    //   // for each input 
    //   for (unsigned int i = 0; i < input_items.size(); i++) {

    //     // Get array of all input items for this input
    //     const unsigned char *in = (const unsigned char *) input_items[i];

    //     cout << "$$ START printing in for input "<< i << "do";
    //     for (unsigned int j = 0; j < ninput_items[j]; j++) {
    //       cout << j;
    //     }
    //     cout << "END \n";

    //     // Get tags in this input item stream
    //     std::vector<tag_t> tags;
    //     get_tags_in_range(tags, i, nitems_read(i), nitems_read(i)+ninput_items[i]);

    //     cout << "$$ NUMBER OF TAGS" << tags.size() << "\n";
    //     // for each tag
    //     for (unsigned int j = 0; j < tags.size(); j++) {
    //       uint64_t offset = tags[j].offset - nitems_read(i) + nitems_written(0) + n_produced;
    //       // if (i =é= d_tag_preserve_head_pos && tags[j].offset == nitems_read(i)) {
    //       //   offset -= n_produced;
    //       // }

    //       // Add tag to output stream at right offset
    //       cout << "TAG KEY" << tags[j].key << "\n";
    //       cout << "TAG VALUE" << tags[j].value << "\n";
    //       add_item_tag(0, offset, tags[j].key, tags[j].value);
    //     }
        
    //     // put sequentially in memory
    //     memcpy((void *) out, (const void *) in, ninput_items[i] * d_itemsize);
    //     out += ninput_items[i] * d_itemsize; // Update pointer
    //     n_produced += ninput_items[i]; // Update produced amount of items
    //   }

    //   return n_produced;
    // }

  } /* namespace packetizr */
} /* namespace gr */

