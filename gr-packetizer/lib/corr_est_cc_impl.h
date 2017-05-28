/* -*- c++ -*- */
/*
 * Copyright 2013 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * GNU Radio is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * GNU Radio is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with GNU Radio; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_PACKETIZER_CORR_EST_CC_IMPL_H
#define INCLUDED_PACKETIZER_CORR_EST_CC_IMPL_H

#include <packetizer/corr_est_cc.h>
#include <gnuradio/filter/fft_filter.h>

using namespace gr::filter;

namespace gr {
  namespace packetizer {

    class corr_est_cc_impl : public corr_est_cc
    {
    private:
      pmt::pmt_t d_src_id;
      std::vector<gr_complex> d_symbols;
      float d_sps;
      unsigned int d_mark_delay, d_stashed_mark_delay;
      double d_thresh, d_stashed_threshold;
      float d_fixed_thresh, d_stashed_fixed_threshold;
      kernel::fft_filter_ccc *d_filter;

      gr_complex *d_corr;
      float *d_corr_mag;

      float d_scale;
      float d_pfa; // probability of false alarm

      bool d_verbose;

      void _set_mark_delay(unsigned int mark_delay);
      void _set_threshold(double threshold);
      void _set_fixed_threshold(float fixed_threshold);

    public:
      corr_est_cc_impl(const std::vector<gr_complex> &symbols,
                       float sps, unsigned int mark_delay,
                       double threshold=0.9, float fixed_threshold=0.9, bool verbose=false);
      ~corr_est_cc_impl();

      std::vector<gr_complex> symbols() const;
      void set_symbols(const std::vector<gr_complex> &symbols);

      unsigned int mark_delay() const;
      void set_mark_delay(unsigned int mark_delay);

      double threshold() const;
      void set_threshold(double threshold);

      float fixed_threshold() const;
      void set_fixed_threshold(float fixed_threshold);

      int work(int noutput_items,
               gr_vector_const_void_star &input_items,
               gr_vector_void_star &output_items);
    };

  } // namespace packetizer
} // namespace gr

#endif /* INCLUDED_PACKETIZER_CORR_EST_CC_IMPL_H */
