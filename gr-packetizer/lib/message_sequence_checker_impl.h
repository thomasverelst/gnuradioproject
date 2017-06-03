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

#ifndef INCLUDED_PACKETIZER_MESSAGE_SEQUENCE_CHECKER_IMPL_H
#define INCLUDED_PACKETIZER_MESSAGE_SEQUENCE_CHECKER_IMPL_H

#include <packetizer/message_sequence_checker.h>
#include <gnuradio/block.h>
#include <pmt/pmt.h>

namespace gr {
  namespace packetizer {

    class message_sequence_checker_impl : public message_sequence_checker
    {
     private:
      std::string d_num_key;
      long d_prev_num;
      long d_packet_fail;
      long d_packet_correct;
      long d_max_seq_nb;
      double d_recent_packet_fail;
      double d_recent_packet_correct;

      void check(pmt::pmt_t msg);

     public:
      message_sequence_checker_impl(const std::string &num_key, const int nb_bits = 12);
      ~message_sequence_checker_impl();

      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace packetizer
} // namespace gr

#endif /* INCLUDED_PACKETIZER_MESSAGE_SEQUENCE_CHECKER_IMPL_H */

