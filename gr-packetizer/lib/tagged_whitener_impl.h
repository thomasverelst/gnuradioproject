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

#ifndef INCLUDED_PACKETIZER_TAGGED_WHITENER_IMPL_H
#define INCLUDED_PACKETIZER_TAGGED_WHITENER_IMPL_H

#include <packetizer/tagged_whitener.h>
#include <packetizer/whitener.h>

namespace gr {
namespace packetizer {

class tagged_whitener_impl : public tagged_whitener
{
private:
  gr::packetizer::kernel::whitener d_whitener;



protected:
  int calculate_output_stream_length(const gr_vector_int &ninput_items);

public:
  tagged_whitener_impl(
    bool use_lfsr,
    std::vector<unsigned char> random_mask,
    int bits_per_byte,
    const std::string &lengthtagname
  );
  ~tagged_whitener_impl();

  // Where all the action really happens
  int work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);

};

} // namespace packetizer
} // namespace gr

#endif /* INCLUDED_packetizer_TAGGED_WHITENER_IMPL_H */

