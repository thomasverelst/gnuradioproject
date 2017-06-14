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


#ifndef INCLUDED_PACKETIZER_MESSAGE_SEQUENCE_CHECKER_H
#define INCLUDED_PACKETIZER_MESSAGE_SEQUENCE_CHECKER_H

#include <packetizer/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace packetizer {

    /*!
     * \brief Checks the sequence number of messages to check for dropped messages (used in combination with 
     * the Extended Packet Decoder to check the sequence number of the packet header)
     * \ingroup packetizer
     *
     */
    class PACKETIZER_API message_sequence_checker : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<message_sequence_checker> sptr;

      /*!
       * \brief Checks the sequence number of messages to check for dropped messages (used in combination with 
       * the Extended Packet Decoder to check the sequence number of the packet header)
       *
       * \param num_key String indicating the message field name
       * \param nb_bits Indicates the number of bits the header field has (to detect overflows)
       */
      static sptr make(const std::string &num_key, const int nb_bits = 12);
    };

  } // namespace packetizer
} // namespace gr

#endif /* INCLUDED_PACKETIZER_MESSAGE_SEQUENCE_CHECKER_H */

