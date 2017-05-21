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
     * \brief <+description of block+>
     * \ingroup packetizer
     *
     */
    class PACKETIZER_API message_sequence_checker : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<message_sequence_checker> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of packetizer::message_sequence_checker.
       *
       * To avoid accidental use of raw pointers, packetizer::message_sequence_checker's
       * constructor is in a private implementation
       * class. packetizer::message_sequence_checker::make is the public interface for
       * creating new instances.
       */
      static sptr make(const std::string &num_key);
    };

  } // namespace packetizer
} // namespace gr

#endif /* INCLUDED_PACKETIZER_MESSAGE_SEQUENCE_CHECKER_H */

