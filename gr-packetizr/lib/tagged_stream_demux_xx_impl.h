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

#ifndef INCLUDED_PACKETIZR_TAGGED_STREAM_DEMUX_XX_IMPL_H
#define INCLUDED_PACKETIZR_TAGGED_STREAM_DEMUX_XX_IMPL_H

#include <packetizr/tagged_stream_demux_xx.h>

namespace gr {
  namespace packetizr {

    class tagged_stream_demux_xx_impl : public tagged_stream_demux_xx
    {
     private:
      size_t d_itemsize;
      std::vector<int> d_splitsize;

     protected:
      int calculate_output_stream_length(const gr_vector_int &ninput_items);

     public:
      tagged_stream_demux_xx_impl(size_t itemsize, const std::string &lengthtagname, const std::vector<int> splitsize);
      ~tagged_stream_demux_xx_impl();

      // Where all the action really happens
      int work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace packetizr
} // namespace gr

#endif /* INCLUDED_PACKETIZR_TAGGED_STREAM_DEMUX_XX_IMPL_H */

