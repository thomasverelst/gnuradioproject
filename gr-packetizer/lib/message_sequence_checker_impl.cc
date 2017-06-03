/* -*- c++ -*- */
/* 
 * Copyright 2017 Thoams Verelst.
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
#include "message_sequence_checker_impl.h"
#include <pmt/pmt.h>
#include <boost/shared_ptr.hpp>
#include <boost/any.hpp>
#include <complex>
#include <string>
#include <stdint.h>
#include <iosfwd>
#include <stdexcept>
#include <math.h>

namespace gr {
  namespace packetizer {

    message_sequence_checker::sptr
    message_sequence_checker::make(const std::string &num_key, const int nb_bits)
    {
      return gnuradio::get_initial_sptr
        (new message_sequence_checker_impl(num_key, nb_bits));
    }

    /*
     * The private constructor
     */
    message_sequence_checker_impl::message_sequence_checker_impl(const std::string &num_key, const int nb_bits)
      : gr::sync_block("message_sequence_checker",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(0, 0, 0)),
      d_num_key(num_key),
      d_prev_num(d_prev_num)
    {
      d_packet_fail = 0;
      d_packet_correct = 0;
      d_recent_packet_fail = 0;
      d_recent_packet_correct = 0;
      d_max_seq_nb = pow(2, nb_bits);
      message_port_register_in(pmt::mp("data"));
      set_msg_handler(pmt::mp("data"), boost::bind(&message_sequence_checker_impl::check, this, _1));

    }

    /*
     * Our virtual destructor.
     */
    message_sequence_checker_impl::~message_sequence_checker_impl()
    {
    }

    void
    message_sequence_checker_impl::check(pmt::pmt_t msg)
    {

      // rough approximation of recent packet loss similar to moving average
      d_recent_packet_fail = d_recent_packet_fail * 0.99;
      d_recent_packet_correct = d_recent_packet_correct * 0.99;

      // There are probably more elegant ways to achieve the same
      if(pmt::is_false(msg)){
        std :: cout << "MSG SEQ CHECK: received incorrect message" << std::endl;
        ++d_packet_fail;
        ++d_recent_packet_fail;

        std:: cout << " Total packet loss (%): " << 100*((float) d_packet_fail)/ (d_packet_fail + d_packet_correct); 
        std:: cout << ", Recent packet loss: (%)" << 100*((float) d_recent_packet_fail)/ (0.00001+d_recent_packet_fail + d_recent_packet_correct); 
        std:: cout << ", Packets failed: " << ((float) d_packet_fail) << ", Total packets"<< (d_packet_fail + d_packet_correct) << std::endl; 

      }else{
        if (!pmt::eq(msg, pmt::PMT_NIL) ) {
          pmt::pmt_t klist(pmt::dict_keys(msg));
          for (size_t i = 0; i < pmt::length(klist); i++) {
            pmt::pmt_t k(pmt::nth(i, klist));
            pmt::pmt_t v(pmt::dict_ref(msg, k, pmt::PMT_NIL));
            if(pmt::symbol_to_string(k) == d_num_key) {
              long curr_num = pmt::to_long(v);
              
              // check check order and compensate for overflowing
              long diff = curr_num - d_prev_num;

              // Check if sequence number has overflowed and number of bits is known
              // d_max_seq_nb is 1 when nb of bits is not known 
              if(diff < 0 && d_max_seq_nb > 1){
                diff += d_max_seq_nb;
              }

              if(diff > 1){
                d_packet_fail += diff;
                d_recent_packet_fail += diff;

                std::cout << "MSG SEQ CHECK: received packet number ";
                std::cout << curr_num << ", previous was "<< d_prev_num;
                std:: cout << std:: endl;
                std:: cout << " Total packet loss (%): " << 100*((float) d_packet_fail)/ (d_packet_fail + d_packet_correct); 
                std:: cout << ", Recent packet loss: (%)" << 100*(d_recent_packet_fail)/ (0.00000001+d_recent_packet_fail + d_recent_packet_correct); 
                std:: cout << ", Packets failed: " << ((float) d_packet_fail) << ", Total packets"<< (d_packet_fail + d_packet_correct) << std::endl; 
              }else if(diff == 1){
                ++d_packet_correct;
                ++d_recent_packet_correct;
              }


              d_prev_num = curr_num;
            }
          }
        }
      }
    }


    int
    message_sequence_checker_impl::work(int noutput_items,
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

