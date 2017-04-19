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

#ifndef INCLUDED_PACKETIZR_TAGGED_WHITEN_IMPL_H
#define INCLUDED_PACKETIZR_TAGGED_WHITEN_IMPL_H

#include <packetizr/tagged_whiten.h>

namespace gr {
  namespace packetizr {

    class tagged_whiten_impl : public tagged_whiten
    {
     private:
      bool d_use_lfsr;
      unsigned char* d_random_mask;
      unsigned int d_random_mask_length;
      int d_bits_per_byte;
      blocks::lfsr_15_1_0 d_lfsr;
      unsigned char d_lsb_mask;


     protected:
      int calculate_output_stream_length(const gr_vector_int &ninput_items);

     public:
      tagged_whiten_impl(
        bool use_lfsr, 
        std::vector<unsigned char> random_mask, 
        int bits_per_byte,
        const std::string &lengthtagname
      );
      ~tagged_whiten_impl();

      // Where all the action really happens
      int work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);

      void do_whitening_lfsr(const unsigned char* data_in, unsigned char* data_out, unsigned int n, unsigned int whitening_offset);

      static unsigned char default_random_mask[4096];
    };

  } // namespace packetizr
} // namespace gr

#endif /* INCLUDED_PACKETIZR_TAGGED_WHITEN_IMPL_H */

