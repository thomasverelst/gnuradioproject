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

#include <stdio.h>
#include <iostream>
using namespace std;


namespace gr {
namespace packetizr {

tagged_stream_demux_xx::sptr
tagged_stream_demux_xx::make(size_t itemsize, const std::string &lengthtagname, const std::vector<int> splitsize)
{
	return gnuradio::get_initial_sptr
	       (new tagged_stream_demux_xx_impl(itemsize, lengthtagname, splitsize));
}

/*
 * The private constructor
 */
tagged_stream_demux_xx_impl::tagged_stream_demux_xx_impl(size_t itemsize, const std::string &lengthtagname, const std::vector<int> splitsize)
	: gr::tagged_stream_block("tagged_stream_demux_xx",
	                          gr::io_signature::make(1, 1, itemsize),
	                          gr::io_signature::make(splitsize.size() + 1, splitsize.size() + 1, itemsize), lengthtagname),
	  d_itemsize(itemsize),
	  d_splitsize(splitsize)
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

	int n_others = ninput_items[0];
	int noutput_items = 0;

	for (unsigned int i = 0; i < d_splitsize.size(); i++) {
		noutput_items = max(noutput_items, d_splitsize[i]);
		n_others -= d_splitsize[i];
	}

	noutput_items = max(noutput_items, n_others);

	return noutput_items;
}

int
tagged_stream_demux_xx_impl::work (int noutput_items,
                                   gr_vector_int &ninput_items,
                                   gr_vector_const_void_star &input_items,
                                   gr_vector_void_star &output_items)
{

	const unsigned char *in = (const unsigned char *) input_items[0];
	int n_produced = 0;
	//cout << "itemsize" << d_itemsize;;
	int n_todo = ninput_items[0]*d_itemsize;


	//TODO memcpy would be faster
	for (unsigned int i = 0; i < d_splitsize.size(); i++) {
		n_produced = max(n_produced, d_splitsize[i]);
		unsigned char *out = (unsigned char *) output_items[i];
		for (unsigned int j = 0 ; j < d_splitsize[i]*d_itemsize; j++) {
			*out = *in;
			out+=1;
			in+=1;
			n_todo--;
			if (n_todo == 0) {
				goto endFor; // hacky, but will do for now
			}
		}
	}

endFor:

	//Put others in last stream
	unsigned char *out = (unsigned char *) output_items[d_splitsize.size()];
	memcpy((void *) out, (void *)in, n_todo);
	n_produced = max(n_produced, n_todo/((int)d_itemsize )); // hacky but will do for now
	// // equal to
	// for (unsigned int k = 0; k < n_todo; k++) {
	// 	*out = *in;
	// 	in++;
	// 	out++;
	// }

	// Tell runtime system how many output items we produced.
	// This will be the length of all output streams!
	return n_produced;

}

} /* namespace packetizr */
} /* namespace gr */

