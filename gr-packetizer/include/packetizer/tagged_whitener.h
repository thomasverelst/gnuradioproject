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


#ifndef INCLUDED_PACKETIZER_TAGGED_WHITENER_H
#define INCLUDED_PACKETIZER_TAGGED_WHITENER_H

#include <packetizer/api.h>
#include <gnuradio/tagged_stream_block.h>
#include <gnuradio/blocks/lfsr_15_1_0.h>

namespace gr {
  namespace packetizer {

    /*!
     * \brief <+description of block+>
     * \ingroup packetizer
     *
     */
    class PACKETIZER_API tagged_whitener : virtual public gr::tagged_stream_block
    {
     public:
      typedef boost::shared_ptr<tagged_whitener> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of packetizer::tagged_whitener.
       *
       * To avoid accidental use of raw pointers, packetizer::tagged_whitener's
       * constructor is in a private implementation
       * class. packetizer::tagged_whitener::make is the public interface for
       * creating new instances.
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

