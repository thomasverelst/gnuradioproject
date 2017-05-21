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

#ifndef INCLUDED_PACKETIZER_MESSAGE_ORDER_CHECK_IMPL_H
#define INCLUDED_PACKETIZER_MESSAGE_ORDER_CHECK_IMPL_H

#include <packetizer/message_order_check.h>
#include <gnuradio/block.h>
#include <pmt/pmt.h>

namespace gr {
  namespace packetizer {

    class message_order_check_impl : public message_order_check
    {
     private:
      std::string d_num_key;
      long d_prev_num;
      // Nothing to declare in this block.

      void check(pmt::pmt_t msg);

     public:
      message_order_check_impl(const std::string &num_key);
      ~message_order_check_impl();

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace packetizer
} // namespace gr

#endif /* INCLUDED_PACKETIZER_MESSAGE_ORDER_CHECK_IMPL_H */

