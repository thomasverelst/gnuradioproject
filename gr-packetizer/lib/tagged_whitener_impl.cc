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
#include "tagged_whitener_impl.h"
#include <stdio.h>
#include <iostream>

using namespace std;

namespace gr {
namespace packetizer {

tagged_whitener::sptr
tagged_whitener::make(
  bool use_lfsr,
  std::vector<unsigned char> random_mask,
  int bits_per_byte,
  const std::string& lengthtagname
)
{
  return gnuradio::get_initial_sptr
         (new tagged_whitener_impl(use_lfsr, random_mask, bits_per_byte, lengthtagname));
}

/*
 * The private constructor
 */
tagged_whitener_impl::tagged_whitener_impl(bool use_lfsr, std::vector<unsigned char> random_mask, int bits_per_byte, const std::string& lengthtagname)
  : gr::tagged_stream_block("tagged_whitener",
                            gr::io_signature::make(1, 1, sizeof(char)),
                            gr::io_signature::make(1, 1, sizeof(char)), lengthtagname)//,
{
  if (use_lfsr) {
    // Initialize usign LFSR
    d_whitener = kernel::whitener(bits_per_byte);
  } else if (random_mask.size() > 0) {
    // Initialize with given mask
    d_whitener = kernel::whitener(random_mask, bits_per_byte);
  } else {
    // Initialize with default random mask
    std::vector<unsigned char> empty_mask;
    d_whitener = kernel::whitener(empty_mask, bits_per_byte);
  }
}

/*
 * Our virtual destructor.
 */
tagged_whitener_impl::~tagged_whitener_impl()
{
}

int
tagged_whitener_impl::calculate_output_stream_length(const gr_vector_int &ninput_items)
{
  return ninput_items[0];
}

int
tagged_whitener_impl::work (int noutput_items,
                          gr_vector_int &ninput_items,
                          gr_vector_const_void_star &input_items,
                          gr_vector_void_star &output_items)
{
  const unsigned char *in = (const unsigned char *) input_items[0];
  unsigned char *out = (unsigned char *) output_items[0];

  set_relative_rate(1.0); // default

  d_whitener.do_whitening(in, out, ninput_items[0], 0);

  // Tell runtime system how many output items we produced.
  return ninput_items[0];
}

} /* namespace packetizer */
} /* namespace gr */

