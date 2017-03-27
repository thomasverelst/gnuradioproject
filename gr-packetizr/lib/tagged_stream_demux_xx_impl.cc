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
#include "tagged_stream_demux_xx_impl.h"

namespace gr {
  namespace packetizr {

    tagged_stream_demux_xx::sptr
    tagged_stream_demux_xx::make(size_t itemsize, const std::string &lengthtagname)
    {
      return gnuradio::get_initial_sptr
        (new tagged_stream_demux_xx_impl(itemsize, lengthtagname));
    }

    /*
     * The private constructor
     */
    tagged_stream_demux_xx_impl::tagged_stream_demux_xx_impl(size_t itemsize, const std::string &lengthtagname)
      : gr::tagged_stream_block("tagged_stream_demux_xx",
              gr::io_signature::make(<+MIN_IN+>, <+MAX_IN+>, sizeof(<+ITYPE+>)),
              gr::io_signature::make(<+MIN_OUT+>, <+MAX_OUT+>, sizeof(<+OTYPE+>)), <+len_tag_key+>)
    {}

    /*
     * Our virtual destructor.
     */
    tagged_stream_demux_xx_impl::~tagged_stream_demux_xx_impl()
    {
    }

    int
    tagged_stream_demux_xx_impl::calculate_output_stream_length(const gr_vector_int &ninput_items)
    {
      int noutput_items = /* <+set this+> */;
      return noutput_items ;
    }

    int
    tagged_stream_demux_xx_impl::work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const <+ITYPE+> *in = (const <+ITYPE+> *) input_items[0];
      <+OTYPE+> *out = (<+OTYPE+> *) output_items[0];

      // Do <+signal processing+>

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace packetizr */
} /* namespace gr */

