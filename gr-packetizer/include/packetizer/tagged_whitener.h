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


#ifndef INCLUDED_PACKETIZER_TAGGED_WHITENER_H
#define INCLUDED_PACKETIZER_TAGGED_WHITENER_H

#include <packetizer/api.h>
#include <gnuradio/tagged_stream_block.h>
#include <gnuradio/blocks/lfsr_15_1_0.h>

namespace gr {
  namespace packetizer {

    /*!
     * \brief Tagged Whitener : whitens and dewhitens incoming datastream
     * \ingroup packetizer
     *
     * \details
     * This block whitens or dewhitens the given data stream. It expects a tagged stream
     * where the tag marks the beginning of the packet and the value is the length 
     * of the value of the packet in chars. To dewhiten, just use the same block with exactly the same settings
     * again on the stream.
     */
    class PACKETIZER_API tagged_whitener : virtual public gr::tagged_stream_block
    {
     public:
      typedef boost::shared_ptr<tagged_whitener> sptr;

      /*!
       * \param use_lfsr Use an LFSR to generate semi-random data (slow)
       * \param random_mask Use the given random mask as XOR mask. Should be a vector of chars (unsigned between 0 and 255).
       *        Parameter not used if use_lfsr is true
       * \param bits_per_byte: number of significant bits per byte
       * \param lengthtagname Name of tag that marks beginning of packet and whose value is the length of the packet. 
       */
      static sptr make(
        const bool use_lfsr, 
        const std::vector<unsigned char> random_mask, 
        const int bits_per_byte,
        const std::string &lengthtagname = "packet_len");
    };

  } // namespace packetizer
} // namespace gr

#endif /* INCLUDED_PACKETIZER_TAGGED_WHITENER_H */

