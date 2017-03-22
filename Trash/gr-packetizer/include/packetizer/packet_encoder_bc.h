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


#ifndef INCLUDED_PACKETIZER_PACKET_ENCODER_BC_H
#define INCLUDED_PACKETIZER_PACKET_ENCODER_BC_H

#include <packetizer/api.h>
#include <gnuradio/tagged_stream_block.h>

namespace gr {
  namespace packetizer {

    /*!
     * \brief <+description of block+>
     * \ingroup packetizer
     *
     */
    class PACKETIZER_API packet_encoder_bc : virtual public gr::tagged_stream_block
    {
     public:
      typedef boost::shared_ptr<packet_encoder_bc> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of packetizer::packet_encoder_bc.
       *
       * To avoid accidental use of raw pointers, packetizer::packet_encoder_bc's
       * constructor is in a private implementation
       * class. packetizer::packet_encoder_bc::make is the public interface for
       * creating new instances.
       */
      static sptr make(int sps,int  header_constel, int payload_constle, int preamble, char* length_tag_key);
    };

  } // namespace packetizer
} // namespace gr

#endif /* INCLUDED_PACKETIZER_PACKET_ENCODER_BC_H */

