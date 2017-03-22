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

#ifndef INCLUDED_TUTORIAL_MY_QPSK_DEMOD_CB_IMPL_H
#define INCLUDED_TUTORIAL_MY_QPSK_DEMOD_CB_IMPL_H

#include <tutorial/my_qpsk_demod_cb.h>

namespace gr {
  namespace tutorial {

    class my_qpsk_demod_cb_impl : public my_qpsk_demod_cb
    {
         private:
      bool d_gray_code;
    

     public:
      my_qpsk_demod_cb_impl(bool gray_code);
      ~my_qpsk_demod_cb_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
      unsigned char
      get_minimum_distances(const gr_complex &sample)
        {
          if (d_gray_code) {
            unsigned char bit0 = 0;
            unsigned char bit1 = 0;
            // The two left quadrants (quadrature component < 0) have this bit set to 1
            if (sample.real() < 0) {
              bit0 = 0x01;
            }
            // The two lower quadrants (in-phase component < 0) have this bit set to 1
            if (sample.imag() < 0) {
              bit1 = 0x01 << 1;
            }
            return bit0 | bit1;
          } else {
            // For non-gray code, we can't simply decide on signs, so we check every single quadrant.
            if (sample.imag() >= 0 and sample.real() >= 0) {
              return 0x00;
            }
            else if (sample.imag() >= 0 and sample.real() < 0) {
              return 0x01;
            }
            else if (sample.imag() < 0 and sample.real() < 0) {
              return 0x02;
            }
            else if (sample.imag() < 0 and sample.real() >= 0) {
              return 0x03;
            }
          }
        }


    };
  } // namespace tutorial
} // namespace gr

#endif /* INCLUDED_TUTORIAL_MY_QPSK_DEMOD_CB_IMPL_H */

