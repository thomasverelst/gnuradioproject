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
#include <gnuradio/digital/packet_header_default.h>
#include <gnuradio/filter/firdes.h>
#include <gnuradio/filter/pfb_arb_resampler.h>
#include "packet_encoder_impl.h"
#include <stdio.h>
#include <iostream>

using namespace std;

namespace gr {
namespace packetizr {

packet_encoder::sptr
packet_encoder::make(const std::vector<int> preamble, digital::constellation_sptr constel_preamble, digital::constellation_sptr constel_header, digital::constellation_sptr  constel_payload, size_t itemsize, const digital::packet_header_default::sptr &header_formatter, const std::string &lengthtagname)
{
  return gnuradio::get_initial_sptr
         (new packet_encoder_impl(preamble, constel_preamble, constel_header, constel_payload, itemsize, header_formatter, lengthtagname));
}

/*
 * The private constructor
 */
packet_encoder_impl::packet_encoder_impl(const std::vector<int> preamble, digital::constellation_sptr constel_preamble, digital::constellation_sptr constel_header, digital::constellation_sptr  constel_payload, size_t itemsize, const digital::packet_header_default::sptr &header_formatter, const std::string &lengthtagname)
  : gr::tagged_stream_block("packet_encoder",
                            gr::io_signature::make(1, 1, sizeof(char)),
                            gr::io_signature::make(1, 1, sizeof(gr_complex)), lengthtagname),
    d_preamble(preamble),
  d_constel_preamble(constel_preamble),
  d_constel_header(constel_header),
  d_constel_payload(constel_payload),
  d_itemsize(1),
  d_header_formatter(header_formatter)

{
  //set_min_output_buffer(128000);
  //set_tag_propagation_policy(TPP_DONT);
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
  nout += d_preamble.size();
  nout += d_header_formatter->header_len()* (8/ d_constel_header->bits_per_symbol());
  nout += ninput_items[0] * (8 / d_constel_payload->bits_per_symbol());
  cout << "EXPECTED LENGTH" << nout << "\n";
  return nout;
}

void
unpack_bits(const unsigned char* packed, unsigned char* unpacked, unsigned int n, unsigned short bits_n) {
  unsigned short newval = 0;
  unsigned short tempindex = 1;
  unsigned short newindex = 0;

  // for every incoming byte
  for (unsigned int i = 0; i < n; i++) {
    char val = packed[i];

    // for every bit of incoming byte
    for (unsigned int j = 0; j < 8; j++) { // TODO hardcoded char length
      newval = (newval << 1) | (val & 0b1);
      if (tempindex == bits_n) {
        unpacked[newindex] = newval;
        newindex++;
        newval = 0;
        tempindex = 0;
      }
      tempindex++;
      val = val >> 1;
    }
  }

  // unsigned short newval = 0;
  // unsigned short tempindex = 1;
  // unsigned short newindex = 0;

  // // for every incoming byte
  // for (unsigned int i = 0; i < n; i++) {
  //   char val = packed[i];

  //   // for every bit of incoming byte
  //   for (unsigned int j = 0; j < 8; j++) { // TODO hardcoded char length
  //     newval = (newval << 1) | (val & 0b1);
  //     if (tempindex == bits_n) {
  //       unpacked[newindex] = newval;
  //       newindex++;
  //       newval = 0;
  //       tempindex = 0;
  //     }
  //     tempindex++;
  //     val = val >> 1;
  //   }
  // }

}

void
interpolate(const gr_complex* input, gr_complex* output, unsigned int input_length, unsigned int factor) {
  for (unsigned int i = 0; i < input_length; i++) {
    output[i * factor] = input[i];
    for (unsigned int j = 1; j < factor; j++) {
      output[i * factor + j] = (0, 0);
    }
  }
}

int
packet_encoder_impl::work (int noutput_items,
                           gr_vector_int &ninput_items,
                           gr_vector_const_void_star &input_items,
                           gr_vector_void_star &output_items)
{
  gr_complex *out = (gr_complex *) output_items[0]; // set pointer where to put output data

  // approximated input/output rate
  set_relative_rate( 8 / d_constel_payload->bits_per_symbol()); // assuming payload is much longer than preamble + header


  /************* PREAMBLE **************/

  // TODO check if valid preamble!
  gr_complex *preamble_symbols = new gr_complex[d_preamble.size()];
  for (unsigned int i = 0; i < d_preamble.size(); i++) {
    //cout << "PREAMBLE VAR "<<i<<" "<<d_preamble[i];
    //preamble_symbols[i] = (1 - d_preamble[i] * 2); // TODO cleanup
    preamble_symbols[i] = d_preamble[i];
  }


  /************* HEADER **************/

  unsigned int header_bps = d_constel_header->bits_per_symbol();
  unsigned int header_length = d_header_formatter->header_len()*8/header_bps; // TODO bytes, bits, symbols?
  cout << "HEADER LENGTH" << header_length;

  /* Generate header */
  unsigned char *header_in = new unsigned char [header_length];
  if (!d_header_formatter->header_formatter(ninput_items[0], header_in)) {
    GR_LOG_FATAL(d_logger, boost::format("header_formatter() returned false (this shouldn't happen). Offending header started at %1%") % nitems_read(0));
    throw std::runtime_error("header formatter returned false.");
  }
  // /* Unpack byte data */

  // Unpack bits in a char to multiple chars with k significant bit (LSB)
  // where k is the number of bits per symbol for the given constellation
  unsigned char *header_unpacked = new unsigned char[header_length];
  unpack_bits(header_in, header_unpacked, d_header_formatter->header_len(), header_bps);
  delete [] header_in;



  /* Mapping */
  gr_complex *header_symbols = new gr_complex[header_length];

  //cout << "PAYLOAD : MAPPING : BITS PER SYMBOL" << d_payload_constel->bits_per_symbol() << "\n";
  for (unsigned int i = 0; i < header_length; i++) {
    unsigned int val = (unsigned int) header_unpacked[i];
    d_constel_header->map_to_points(val, &header_symbols[i]);
    //cout << " value " << val << " mapped to constellation point " << payload_symbols[j] << "\n";
  }
  delete [] header_unpacked;

 


  /************* PAYLOAD **************/

  const unsigned char *payload_in = (const unsigned char *) input_items[0];
  unsigned int payload_bps = d_constel_payload->bits_per_symbol();
  unsigned int payload_length = ninput_items[0] * 8 / payload_bps; // Payload length in bytes


  /* Unpack payload data */

  // Unpack bits in a char to multiple chars with k significant bit (LSB)
  // where k is the number of bits per symbol for the given constellation
  //consume(1, ninput_items[1]);
  unsigned char *payload_unpacked = new unsigned char[payload_length];
  unpack_bits(payload_in, payload_unpacked, ninput_items[0], payload_bps);

  /* Mapping */
  gr_complex *payload_symbols = new gr_complex[payload_length];

  //cout << "PAYLOAD : MAPPING : BITS PER SYMBOL" << d_payload_constel->bits_per_symbol() << "\n";
  for (unsigned int i = 0; i < payload_length; i++) {
    unsigned int val = (unsigned int) payload_unpacked[i];
    d_constel_payload->map_to_points(val, &payload_symbols[i]);
    //cout << " value " << val << " mapped to constellation point " << payload_symbols[j] << "\n";
  }
  delete [] payload_unpacked;


  /************* COMBINING **************/

  /* CONCATENATE PREAMBLE + HEADER + PAYLOAD */
  unsigned int total_length = d_preamble.size() + header_length + payload_length;
  //cout << "TOTAL_LENGTH in complex samples, before oversampling "<<total_length<<"\n";
  cout << "PREAMBLE LENGTH " << d_preamble.size() << " HEADER LENGTH "<<header_length << " PAYLOAD_LENGTH" << payload_length << "\n";
  gr_complex *signal_symbols = new gr_complex[total_length];
  unsigned int index = 0;
  for (unsigned int i = 0; i < d_preamble.size(); i++) {
    signal_symbols[index] = preamble_symbols[i];
    index += 1;
  }
  for (unsigned int i = 0; i < header_length; i++) {
    signal_symbols[index] = header_symbols[i];
    index += 1;
  }
  for (unsigned int i = 0; i < payload_length; i++) {
    signal_symbols[index] = payload_symbols[i];
    index += 1;
  }
  delete [] preamble_symbols;
  delete [] header_symbols;
  delete [] payload_symbols;

  // Maybe faster with memcpy but risky...

  /* Print symbols*/
  // for (unsigned int i = 0; i < total_length; i++) {
  //   cout << signal_symbols[i] << "\n";
  // }


  /* PLACE RESULT IN MEMORY */

  //memcpy((void *) out, (const void *) signal_mod, os_length);
  for (unsigned int i = 0; i < total_length; i++) {
    *out =  signal_symbols[i] ;
    out += 1;
  }
  delete [] signal_symbols;
  
  //out += os_length; // Update pointer
  int n_produced = total_length; // Update produced of item amount

  // return
  return n_produced;





























  // /* PROCESS HEADER DATA */

  // // Get pointer to array of all input items from header data input
  // const unsigned char *header_in = (const unsigned char *) input_items[0];
  // unsigned int header_bps = d_header_constel->bits_per_symbol(); // TODO can be defined outside work
  // unsigned int header_length = ninput_items[0] * 8 / header_bps; // Payload length in bytes

  // // Get tags in this input item stream
  // // std::vector<tag_t> tags;
  // // get_tags_in_range(tags, 0, nitems_read(0), nitems_read(0) + ninput_items[0]);
  // // cout << "Found # tags" << tags.size() << "\n";
  // // for (unsigned int j = 0; j < tags.size(); j++) {
  // //   uint64_t offset = tags[j].offset - nitems_read(0) + nitems_written(0) + n_produced;
  // //   cout <<"Found tag with key " << tags[j].key << " and value " << tags[j].value << " and offset "<<tags[j].offset << " and "<< offset << "\n";
  // //   // if (i =é= d_tag_preserve_head_pos && tags[j].offset == nitems_read(i)) {
  // //   //   offset -= n_produced;
  // //   // }

  // //   // Add tag to output stream at right offset
  // //   add_item_tag(0, offset, tags[j].key, tags[j].value);
  // // }

  // /* BYTE UNPACKING FOR HEADER DATA */

  // // Unpack bits in a char to multiple chars with k significant bit (LSB)
  // // where k is the number of bits per symbol for the given constellation
  // //consume(0, ninput_items[0]);
  // unsigned char *header_unpacked = new unsigned char[header_length];
  // unpack_bits(header_in, header_unpacked, ninput_items[0], header_bps);


  // /* MAPPING OF HEADER DATA*/
  // gr_complex *header_symbols = new gr_complex[header_length];

  // //cout << "PAYLOAD : MAPPING : BITS PER SYMBOL" << d_payload_constel->bits_per_symbol() << "\n";
  // for (unsigned int j = 0; j < header_length; j++) {
  //   unsigned int val = (unsigned int) header_unpacked[j];
  //   d_header_constel->map_to_points(val, &header_symbols[j]);
  //   //cout << " value " << val << " mapped to constellation point " << payload_symbols[j] << "\n";
  // }
  // delete [] header_unpacked;







  // /* PROCESS PAYLOAD DATA*/

  // const unsigned char *payload_in = (const unsigned char *) input_items[1];
  // unsigned int payload_bps = d_payload_constel->bits_per_symbol(); // TODO can be defined ouside work
  // unsigned int payload_length = ninput_items[1] * 8 / payload_bps; // Payload length in bytes

  // // Get tags in this input item stream
  // // get_tags_in_range(tags, 1, nitems_read(1), nitems_read(1) + ninput_items[1]);

  // // for (unsigned int j = 0; j < tags.size(); j++) {
  // //   uint64_t offset = tags[j].offset - nitems_read(1) + nitems_written(0) + n_produced;
  // //   cout <<"Found tag with key " << tags[j].key << " and value " << tags[j].value << " and offset "<<tags[j].offset << " and "<< offset << "\n";
  // //   // if (i =é= d_tag_preserve_head_pos && tags[j].offset == nitems_read(i)) {
  // //   //   offset -= n_produced;
  // //   // }

  // //   // Add tag to output stream at right offset
  // //   add_item_tag(0, offset, tags[j].key, tags[j].value);
  // // }


  // /* BYTE UNPACKING FOR PAYLOAD DATA */

  // // Unpack bits in a char to multiple chars with k significant bit (LSB)
  // // where k is the number of bits per symbol for the given constellation
  // //consume(1, ninput_items[1]);
  // unsigned char *payload_unpacked = new unsigned char[payload_length];
  // unpack_bits(payload_in, payload_unpacked, ninput_items[1], payload_bps);


  // /* MAPPING OF PAYLOAD DATA*/
  // gr_complex *payload_symbols = new gr_complex[payload_length];

  // //cout << "PAYLOAD : MAPPING : BITS PER SYMBOL" << d_payload_constel->bits_per_symbol() << "\n";
  // for (unsigned int j = 0; j < payload_length; j++) {
  //   unsigned int val = (unsigned int) payload_unpacked[j];
  //   d_payload_constel->map_to_points(val, &payload_symbols[j]);
  //   //cout << " value " << val << " mapped to constellation point " << payload_symbols[j] << "\n";
  // }
  // delete [] payload_unpacked;




  // /* CONCATENATE PREAMBLE + HEADER + PAYLOAD */
  // unsigned int total_length = d_preamble.size() + header_length + payload_length;
  // //cout << "TOTAL_LENGTH in complex samples, before oversampling "<<total_length<<"\n";
  // cout << "PREAMBLE LENGTH " << d_preamble.size() << " HEADER LENGTH "<<header_length << " PAYLOAD_LENGTH" << payload_length << "\n";
  // gr_complex *signal_symbols = new gr_complex[total_length];
  // unsigned int index = 0;
  // for (unsigned int i = 0; i < d_preamble.size(); i++) {
  //   signal_symbols[index] = preamble_symbols[i];
  //   index += 1;
  // }
  // for (unsigned int i = 0; i < payload_length; i++) {
  //   signal_symbols[index] = payload_symbols[i];
  //   index += 1;
  // }
  // delete [] header_symbols;
  // delete [] payload_symbols;

  // // Maybe faster with memcpy but risky...

  // /* Print symbols*/
  // // for (unsigned int i = 0; i < total_length; i++) {
  // //   cout << signal_symbols[i] << "\n";
  // // }


  // /* MODULATION OF PREAMBLE + HEADER + PAYLOAD */
  // unsigned int os_length = total_length;
  // gr_complex *signal_mod = new gr_complex[os_length];

  // // TODO should be defined outside of work function for speed reasons
  // // gr::filter::kernel::pfb_arb_resampler_ccf rrc_filter = gr::filter::kernel::pfb_arb_resampler_ccf(d_sps, d_rrc_taps, d_nfilts);
  // //// rrc_filter.filter(signal_mod, signal_symbols, total_length, (int&) n_read);
  // //interpolate(signal_symbols, signal_mod, total_length, d_sps);
  // delete [] signal_symbols;

  // //Print modulated output
  // //cout << "Modulated symbols: ";
  // //for(unsigned int j = 0; j < os_length; j++){
  //   //gr_complex test(3.14, 0.64);
  //   //signal_mod[j] = test;
  // //  cout << " " << j <<":" << signal_mod[j] << " \n ";
  // //}
  // //cout << "\n";

  // /* PLACE RESULT  IN MEMORY */

  // //memcpy((void *) out, (const void *) signal_mod, os_length);
  // for (unsigned int j = 0; j < os_length; j++) {
  //   *out =  signal_symbols[j] ;
  //   out += 1;
  // }
  // delete [] signal_mod;
  // //out += os_length; // Update pointer
  // n_produced += os_length; // Update produced of item amount

  // return
  //return n_produced;
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

