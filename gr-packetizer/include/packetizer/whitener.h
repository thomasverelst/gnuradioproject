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


#ifndef INCLUDED_PACKETIZER_WHITENER_H
#define INCLUDED_PACKETIZER_WHITENER_H

#include <packetizer/api.h>
#include <limits.h>
#include <vector>
#include <gnuradio/blocks/lfsr_15_1_0.h>

namespace gr {
namespace packetizer {
namespace kernel {

/*!
 * \brief Whitener class
 * Helper class to whiten binary data.
 *
 */
class PACKETIZER_API whitener
{
private:
  bool d_use_lfsr;
  blocks::lfsr_15_1_0 d_lfsr;
  unsigned char* d_random_mask;
  unsigned int d_random_mask_length;
  unsigned char d_lsb_mask;

public:
  ~whitener();

  /*!
  * Initiates a whitener for 8 significant bits per byte using an LFSR.
  */
  whitener();

  /*!
  * Initiates a whitener for \p bits_per_byte significant bits per byte 
  * using the given \p random_mask to XOR data with.
  * If \p random_mask is an empty vector (for example 
  * initialized as std::vector<unsigned char> empty_mask;),
  * a precomputed random mask will be used.
  */
  whitener(std::vector<unsigned char> random_mask, int bits_per_byte);

  /*!
  * Initiates a whitener for \p bits_per_byte significant bits per byte
  * using an LFSR.
  */
  whitener(int bits_per_byte);

  /* Builds a mask where the lower bits_per_byte bits are 1. F
  * E.g: if bits_per_byte = 3, the output will be 0000111
  */
  static unsigned char
  lsb_mask(int bits_per_byte) {
    return (((unsigned char) - 1) >> ((sizeof(unsigned char) * CHAR_BIT) - (unsigned char) bits_per_byte));
  }

  /*!
  * Do the whitening. Start reading data in at pointer \p data_in
  * Starts outputting data at \p data_out
  * Processes \p data_length bytes of data.
   */
  void
  do_whitening(const unsigned char* data_in, unsigned char* data_out, unsigned int data_length, unsigned int whitening_offset);

  static unsigned char default_random_mask[4096];
};

} // namespace kernel
} // namespace packetizer
} // namespace gr

#endif /* INCLUDED_PACKETIZER_WHITENER_H */

