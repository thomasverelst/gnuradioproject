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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include <gnuradio/digital/constellation.h>
#include <gnuradio/digital/packet_header_default.h>
#include "packet_encoder_impl.h"
#include <stdio.h>
#include <iostream>
#include <math.h>

namespace gr {
namespace packetizer {

packet_encoder::sptr
packet_encoder::make(
  const std::vector<int> preamble,
  const digital::constellation_sptr constel_header,
  const digital::constellation_sptr constel_payload,
  const digital::packet_header_default::sptr& header_formatter,
  const bool diff_header,
  const bool diff_payload,
  const std::string& lengthtagname,
  int zero_padding,
  bool whiten,
  size_t itemsize)
{
  return gnuradio::get_initial_sptr(
           new packet_encoder_impl(
             preamble,
             constel_header,
             constel_payload,
             header_formatter,
             diff_header,
             diff_payload,
             lengthtagname,
             zero_padding,
             whiten,
             itemsize));
}

/*
* The private constructor
*/
packet_encoder_impl::packet_encoder_impl(
  const std::vector<int> preamble,
  const digital::constellation_sptr constel_header,
  const digital::constellation_sptr constel_payload,
  const digital::packet_header_default::sptr& header_formatter,
  const bool diff_header,
  const bool diff_payload,
  const std::string& lengthtagname,
  const int zero_padding,
  const bool whiten,
  const size_t itemsize)
  : gr::tagged_stream_block("packet_encoder",
                            gr::io_signature::make(1, 1, sizeof(char)),
                            gr::io_signature::make(1, 1, sizeof(gr_complex)), lengthtagname)
  , d_preamble(preamble)
  , d_constel_header(constel_header)
  , d_diff_header(diff_header)
  , d_constel_payload(constel_payload)
  , d_diff_payload(diff_payload)
  , d_zero_padding(zero_padding)
  , d_whiten(whiten)
  , d_itemsize(1)
  , d_header_formatter(header_formatter)
  , d_last_diff(0)
  , d_last_diff_payload(0)

{
  //set_min_output_buffer(128000);
  set_tag_propagation_policy(TPP_DONT); // Not very clean...
  if (whiten) {
    std::vector<unsigned char> empty_mask;
    d_whitener = kernel::whitener(empty_mask, 1);
  }
}

/*
* Our virtual destructor.
*/
packet_encoder_impl::~packet_encoder_impl()
{
}

int
packet_encoder_impl::calculate_output_stream_length(const gr_vector_int& ninput_items)
{
  int nout = 0;
  nout += d_preamble.size();
  nout += ceil((float) d_header_formatter->header_len() / d_constel_header->bits_per_symbol());
  nout += ceil((float) ninput_items[0] / d_constel_payload->bits_per_symbol());
  nout += d_zero_padding;
  //std::cout << "PACKET_ENCODER : expected length " << nout << "\n";
  return nout;
}

void
pack_bits_msb(const unsigned char* unpacked, unsigned char* packed, unsigned int n, unsigned int bits_n)
{
   unsigned char newval = 0;
   unsigned int newindex = 0;
   unsigned int shift_val = bits_n;

   
   // MSB first packing (filling unpacked with MSB first)
   // In case there are not enough bits to fill the last byte, zero-bits will be used to fill up the space
   // Incoming stream (without leading zeros) (13 elements):  1 0 1 1 0 1 0 0 0 1 0 0 1
   // Outgoing stream:  00001011 00000100 00000100 00001000
   // The three last bits are zero


   // for every incoming byte
   for (unsigned int i = 0; i < n; i++) {
      if (shift_val == 0) {
         packed[newindex++] = newval;
         newval = 0;
         shift_val = bits_n;
      }

      // Copy bit by bit, filling the new value LSB first
      newval = newval | ((unpacked[i] & 0b1) << --shift_val);
   }

   // Fill last byte
   packed[newindex] = newval;
}


int
packet_encoder_impl::work(int noutput_items,
                          gr_vector_int& ninput_items,
                          gr_vector_const_void_star& input_items,
                          gr_vector_void_star& output_items)
{
  gr_complex* out = (gr_complex*)output_items[0]; // set pointer where to put output data

  // approximated input/output rate
  int nout = 0; // in symbols
  nout += d_preamble.size();
  nout += ceil((float) d_header_formatter->header_len() / d_constel_header->bits_per_symbol());
  nout += ceil((float) ninput_items[0] / d_constel_payload->bits_per_symbol());
  nout += d_zero_padding;
  set_relative_rate(nout / ninput_items[0]); // assuming payload is much longer than preamble + header

  // Some variables
  unsigned int header_bps = d_constel_header->bits_per_symbol();
  unsigned int header_length = d_header_formatter->header_len(); // Header length in number of symbols

  unsigned int payload_bps = d_constel_payload->bits_per_symbol();
  unsigned int payload_length = ceil((float) ninput_items[0] / payload_bps); // Payload length in symbols


  /************* PREAMBLE **************/
  gr_complex* preamble_symbols = new gr_complex[d_preamble.size()];
  for (unsigned int i = 0; i < d_preamble.size(); i++) {
    preamble_symbols[i] = d_preamble[i];
  }

  /************* HEADER **************/
  /* Generate header */
  unsigned char* header_in = new unsigned char[header_length];
  if (!d_header_formatter->header_formatter(ninput_items[0], header_in)) {
    GR_LOG_FATAL(d_logger, boost::format("header_formatter() returned false (this shouldn't happen). Offending header started at %1%") % nitems_read(0));
    throw std::runtime_error("header formatter returned false.");
  }

  /* Apply differental code, if  needed */
  if(d_diff_header){
    int order = (d_constel_header->points()).size();
    for(int i = 0; i < header_length; i++) {
      header_in[i] = (header_in[i] + d_last_diff) % order;
      d_last_diff = header_in[i];
    }
  }

  /* Mapping */

  gr_complex* header_symbols = new gr_complex[header_length];

  for (unsigned int i = 0; i < header_length; i++) {
    unsigned int val = (unsigned int)header_in[i];
    d_constel_header->map_to_points(val, &header_symbols[i]);
  }

  /************* PAYLOAD **************/

  unsigned char* payload_in = (unsigned char*)input_items[0];
  //unsigned char* payload_data = new unsigned char[ninput_items[0]];

  /* Whitening */
  if (d_whiten) {
    d_whitener.do_whitening(payload_in, payload_in, ninput_items[0], 0);
  }


  /* Pack payload data */
  unsigned char* payload_packed = new unsigned char[payload_length];
  pack_bits_msb(payload_in, payload_packed, ninput_items[0], payload_bps);

  /* Apply differental code, if needed */
  if(d_diff_payload){
    int order = (d_constel_payload->points()).size();
    for(int i = 0; i < payload_length; i++) {
      payload_packed[i] = (payload_packed[i] + d_last_diff_payload) % order;
      d_last_diff_payload = payload_packed[i];
    }
  }

  /* Mapping */
  gr_complex* payload_symbols = new gr_complex[payload_length];

  for (unsigned int i = 0; i < payload_length; i++) {
    unsigned int val = (unsigned int)payload_packed[i];
    d_constel_payload->map_to_points(val, &payload_symbols[i]);
  }
  delete[] payload_packed;

  /************* PACKET BUILDER **************/

  /* CONCATENATE PREAMBLE + HEADER + PAYLOAD */
  unsigned int total_length = d_preamble.size() + header_length + payload_length + d_zero_padding; // Total length in symbols
  // std::cout << "PACKET ENCODER: total length in complex samples "<<total_length<<"\n";
  // std::cout << "PACKET ENCODER: preamble_length " << d_preamble.size() << ", header length "<<header_length << ", payload length" << payload_length << ", padding length" << d_zero_padding << "\n";
  gr_complex* signal_symbols = new gr_complex[total_length];
  unsigned int index = 0;
  for (unsigned int i = 0; i < d_zero_padding; i++) {
    signal_symbols[index] = 0;
    index += 1;
  }
  for (unsigned int i = 0; i < d_preamble.size(); i++) {
    signal_symbols[index] = preamble_symbols[i];
    // std::cout << preamble_symbols[i] << "\n";
    index += 1;
  }
  for (unsigned int i = 0; i < header_length; i++) {
    // std::cout << header_symbols[i] << "\n";
    signal_symbols[index] = header_symbols[i];
    index += 1;
  }
  for (unsigned int i = 0; i < payload_length; i++) {
    signal_symbols[index] = payload_symbols[i];
    index += 1;
  }
  delete[] preamble_symbols;
  delete[] header_symbols;
  delete[] payload_symbols;

  /* PUT RESULT IN MEMORY */
  // Note: concatenate and memcpy could be easily combined...
  memcpy((void *) out, (const void *) signal_symbols, total_length * sizeof(gr_complex));
  delete[] signal_symbols;

  int n_produced = total_length; // Update produced of item amount
  return n_produced;
}

} /* namespace packetizer */
} /* namespace gr */