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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "message_order_check_impl.h"
#include <pmt/pmt.h>
#include <boost/shared_ptr.hpp>
#include <boost/any.hpp>
#include <complex>
#include <string>
#include <stdint.h>
#include <iosfwd>
#include <stdexcept>

namespace gr {
  namespace packetizer {

    message_order_check::sptr
    message_order_check::make(const std::string &num_key)
    {
      return gnuradio::get_initial_sptr
        (new message_order_check_impl(num_key));
    }

    /*
     * The private constructor
     */
    message_order_check_impl::message_order_check_impl(const std::string &num_key)
      : gr::sync_block("message_order_check",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(0, 0, 0)),
      d_num_key(num_key),
      d_prev_num(d_prev_num)
    {
      message_port_register_in(pmt::mp("data"));
      set_msg_handler(pmt::mp("data"), boost::bind(&message_order_check_impl::check, this, _1));

    }

    /*
     * Our virtual destructor.
     */
    message_order_check_impl::~message_order_check_impl()
    {
    }

    void
    message_order_check_impl::check(pmt::pmt_t msg)
    {
      // There are probably more elegant ways to achieve the same
      if(pmt::is_false(msg)){
        std :: cout << "MESSAGE ORDER CHECK: received incorrect message" << std::endl;
      }else{
        if (!pmt::eq(msg, pmt::PMT_NIL) ) {
          pmt::pmt_t klist(pmt::dict_keys(msg));
          for (size_t i = 0; i < pmt::length(klist); i++) {
            pmt::pmt_t k(pmt::nth(i, klist));
            pmt::pmt_t v(pmt::dict_ref(msg, k, pmt::PMT_NIL));
            if(pmt::symbol_to_string(k) == d_num_key) {
              long curr_num = pmt::to_long(v);

              // check if received packet number is not 0 (to avoid 
              // false positives when overflowing) and check order
              if(curr_num != 0 && curr_num != d_prev_num + 1 ){
                std::cout << "MESSAGE ORDER CHECK: received packet with number ";
                std::cout << curr_num << " while previous was "<< d_prev_num << std::endl;
              }
              d_prev_num = curr_num;
            }
          }
        }
      }
    }


    int
    message_order_check_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      //const <+ITYPE+> *in = (const <+ITYPE+> *) input_items[0];

      // Do <+signal processing+>

      // Tell runtime system how many output items we produced.
      return 0;
    }

  } /* namespace packetizer */
} /* namespace gr */

