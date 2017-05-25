/* -*- c++ -*- */
/*
 * Copyright 2015 Free Software Foundation, Inc.
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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif





#include <gnuradio/io_signature.h>
#include <gnuradio/math.h>
#include "corr_est_cc_impl.h"
#include <volk/volk.h>
#include <boost/format.hpp>
#include <boost/math/special_functions/round.hpp>
#include <gnuradio/filter/pfb_arb_resampler.h>
#include <gnuradio/filter/firdes.h>
#include <float.h>

namespace gr {
  namespace packetizer {

    corr_est_cc::sptr
    corr_est_cc::make(const std::vector<gr_complex> &symbols,
                      float sps, unsigned int mark_delay,
                      double threshold, float abs_threshold, bool verbose)
    {
      return gnuradio::get_initial_sptr
        (new corr_est_cc_impl(symbols, sps, mark_delay, threshold, abs_threshold, verbose));
    }

    corr_est_cc_impl::corr_est_cc_impl(const std::vector<gr_complex> &symbols,
                                       float sps, unsigned int mark_delay,
                                       double threshold, float abs_threshold, bool verbose)
      : gr::sync_block("corr_est_cc",
                   io_signature::make(1, 1, sizeof(gr_complex)),
                   io_signature::make(1, 2, sizeof(gr_complex))),
        d_src_id(pmt::intern(alias())),
        d_verbose(verbose)
    {
      d_sps = sps;

      // In order to easily support the optional second output,
      // don't deal with an unbounded max number of output items.
      // For the common case of not using the optional second output,
      // this ensures we optimally call the volk routines.
      const size_t nitems = 24*1024;
      set_max_noutput_items(nitems);
      d_corr = (gr_complex *)
               volk_malloc(sizeof(gr_complex)*nitems, volk_get_alignment());
      d_corr_mag = (float *)
                   volk_malloc(sizeof(float)*nitems, volk_get_alignment());

      // Create time-reversed conjugate of symbols
      d_symbols = symbols;
      for(size_t i=0; i < d_symbols.size(); i++) {
          d_symbols[i] = conj(d_symbols[i]);
      }
      std::reverse(d_symbols.begin(), d_symbols.end());

      set_mark_delay(mark_delay);
      set_threshold(threshold);
      set_abs_threshold(abs_threshold);

      // Correlation filter
      d_filter = new kernel::fft_filter_ccc(1, d_symbols);

      // Per comments in gr-filter/include/gnuradio/filter/fft_filter.h,
      // set the block output multiple to the FFT filter kernel's internal,
      // assumed "nsamples", to ensure the scheduler always passes a
      // proper number of samples.
      int nsamples;
      nsamples = d_filter->set_taps(d_symbols);
      set_output_multiple(nsamples);

      // It looks like the kernel::fft_filter_ccc stashes a tail between
      // calls, so that contains our filtering history (I think).  The
      // fft_filter_ccc block (which calls the kernel::fft_filter_ccc) sets
      // the history to 1 (0 history items), so let's follow its lead.
      //set_history(1);

      // We'll (ab)use the history for our own purposes of tagging back in time.
      // Keep a history of the length of the sync word to delay for tagging.
      set_history(d_symbols.size()+1);

      declare_sample_delay(1, 0);
      declare_sample_delay(0, d_symbols.size());

      // Setting the alignment multiple for volk causes problems with the
      // expected behavior of setting the output multiple for the FFT filter.
      // Don't set the alignment multiple.
      //const int alignment_multiple =
      //  volk_get_alignment() / sizeof(gr_complex);
      //set_alignment(std::max(1,alignment_multiple));

      d_scale = 1.0f;
    }

    corr_est_cc_impl::~corr_est_cc_impl()
    {
      delete d_filter;
      volk_free(d_corr);
      volk_free(d_corr_mag);
    }

    std::vector<gr_complex>
    corr_est_cc_impl::symbols() const
    {
      return d_symbols;
    }

    void
    corr_est_cc_impl::set_symbols(const std::vector<gr_complex> &symbols)
    {
      gr::thread::scoped_lock lock(d_setlock);

      d_symbols = symbols;

      // Per comments in gr-filter/include/gnuradio/filter/fft_filter.h,
      // set the block output multiple to the FFT filter kernel's internal,
      // assumed "nsamples", to ensure the scheduler always passes a
      // proper number of samples.
      int nsamples;
      nsamples = d_filter->set_taps(d_symbols);
      set_output_multiple(nsamples);

      // It looks like the kernel::fft_filter_ccc stashes a tail between
      // calls, so that contains our filtering history (I think).  The
      // fft_filter_ccc block (which calls the kernel::fft_filter_ccc) sets
      // the history to 1 (0 history items), so let's follow its lead.
      //set_history(1);

      // We'll (ab)use the history for our own purposes of tagging back in time.
      // Keep a history of the length of the sync word to delay for tagging.
      set_history(d_symbols.size()+1);

      declare_sample_delay(1, 0);
      declare_sample_delay(0, d_symbols.size());

      _set_mark_delay(d_stashed_mark_delay);
      _set_threshold(d_stashed_threshold);
    }

    unsigned int
    corr_est_cc_impl::mark_delay() const
    {
      return d_mark_delay;
    }

    void
    corr_est_cc_impl::_set_mark_delay(unsigned int mark_delay)
    {
      d_stashed_mark_delay = mark_delay;

      if(mark_delay >= d_symbols.size()) {
        d_mark_delay = d_symbols.size()-1;
        GR_LOG_WARN(d_logger, boost::format("set_mark_delay: asked for %1% but due "
                                            "to the symbol size constraints, "
                                            "mark delay set to %2%.") \
                    % mark_delay % d_mark_delay);
      }
      else {
        d_mark_delay = mark_delay;
      }
    }

    void
    corr_est_cc_impl::set_mark_delay(unsigned int mark_delay)
    {
      gr::thread::scoped_lock lock(d_setlock);
      _set_mark_delay(mark_delay);
    }

    double
    corr_est_cc_impl::threshold() const
    {
      return d_thresh;
    }


    float
    corr_est_cc_impl::abs_threshold() const
    {
      return d_abs_thresh;
    }


    void
    corr_est_cc_impl::_set_threshold(double threshold)
    {
      d_stashed_threshold = threshold;
      d_pfa = (float) -log(1.0-threshold);
    }

    void
    corr_est_cc_impl::set_threshold(double threshold)
    {
      gr::thread::scoped_lock lock(d_setlock);
      _set_threshold(threshold);
    }

    void
    corr_est_cc_impl::_set_abs_threshold(float abs_threshold)
    {
      d_stashed_abs_threshold = abs_threshold;
      // Compute a correlation threshold.
      // Compute the value of the discrete autocorrelation of the matched
      // filter with offset 0 (aka the autocorrelation peak).
      float corr = 0;
      for(size_t i = 0; i < d_symbols.size(); i++){
        corr += abs(d_symbols[i]*conj(d_symbols[i]));
      }
      d_abs_thresh = abs_threshold*corr*corr;
    }

    void
    corr_est_cc_impl::set_abs_threshold(float abs_threshold)
    {
      gr::thread::scoped_lock lock(d_setlock);
      _set_abs_threshold(abs_threshold);
    }

    int
    corr_est_cc_impl::work(int noutput_items,
                           gr_vector_const_void_star &input_items,
                           gr_vector_void_star &output_items)
    {
      gr::thread::scoped_lock lock(d_setlock);

      const gr_complex *in = (gr_complex *)input_items[0];
      gr_complex *out = (gr_complex*)output_items[0];
      gr_complex *corr;

      // If correlation values should be outputted, immediately use output buffer
      if (output_items.size() > 1){
          corr = (gr_complex *) output_items[1];
      }else{
          corr = d_corr;
      }

      // Our correlation filter length
      // history() - 1 is same as d_symbols.size()
      unsigned int hist_len = history() - 1;

      // Calculate the correlation of the non-delayed input with the
      // known symbols.
      d_filter->filter(noutput_items, &in[hist_len], corr); // nitems, input, output

      // Find the magnitude squared of the correlation
      volk_32fc_magnitude_squared_32f(&d_corr_mag[0], corr, noutput_items);

      // Calculate the average squared correlation magnitude of the input
      // float detection = 0;
      // for(int i = 0; i < noutput_items; i++) {
      //  detection += d_corr_mag[i];
      // }
      // detection /= static_cast<float>(noutput_items);

      // //Multiply by our threshold factor
      // detection *= d_pfa;
      // add_item_tag(1, nitems_written(0), pmt::intern("START"),
      //                pmt::from_double(detection), d_src_id);
      // add_item_tag(0, nitems_written(0)+noutput_items, pmt::intern("END"),
      //                pmt::from_double(d_cnt), d_src_id);

      int isps = (int)(d_sps + 0.5f);
      int i = 0;
      while(i < noutput_items) {

        // Look for the correlator output to cross the threshold.
        // Sum power over two consecutive symbols in case we're offset
        // in time. If off by 1/2 a symbol, the peak of any one point
        // is much lower.
        float corr_mag = d_corr_mag[i] + d_corr_mag[i+1];

        // Dynamic threshold
        // Calculate the average squared correlation magnitude of the input
        float detection = 0;
        for(int k = 0; k < hist_len; k++) {
          detection += d_corr_mag[i+k];
        }
        detection /= static_cast<float>(hist_len);

        // Multiply by our threshold factor
        detection *= d_pfa;


        if(corr_mag <= 4*detection || corr_mag <= d_abs_thresh) {
          // Move detection threshold to next sample
          //detection += (d_corr_mag[i+hist_len-1]*d_pfa - d_corr_mag[i-1]*d_pfa)/static_cast<float>(hist_len);
          i++;
          continue;
        }
        if(d_verbose)
          std::cout << "Detection with correlation magnitude "<<corr_mag<<" versus adaptive threshold of "<<4*detection << " and fixed threshold of "<<d_abs_thresh<<std::endl;

        // Go to (just past) the current correlator output peak
        while ((i < (noutput_items-1)) &&
               (d_corr_mag[i] < d_corr_mag[i+1])) {
          // Move detection threshold to next sample
          //detection += (d_corr_mag[i+hist_len-1]*d_pfa-d_corr_mag[i-1]*d_pfa)/static_cast<float>(hist_len);
          i++;
        }
        // Delaying the primary signal output by the matched filter
        // length using history(), means that the the peak output of
        // the matched filter aligns with the start of the desired
        // sync word in the primary signal output.  This corr_start
        // tag is not offset to another sample, so that downstream
        // data-aided blocks (like adaptive equalizers) know exactly
        // where the start of the correlated symbols are.
        add_item_tag(0, nitems_written(0) + i, pmt::intern("corr_start"),
                     pmt::from_double(d_corr_mag[i]), d_src_id);
       

#if 0
        // Use Parabolic interpolation to estimate a fractional
        // sample delay. There are more accurate methods as
        // the sample delay estimate using this method is biased.
        // But this method is simple and fast.
        // center between [-0.5,0.5] units of samples
        // Paper Reference: "Discrete Time Techniques for Time Delay
        // Estimation" G. Jacovitti and G. Scarano
        double center = 0.0;
        if( i > 0 && i < (noutput_items - 1 )){
          double nom = d_corr_mag[i-1]-d_corr_mag[i+1];
          double denom = 2*(d_corr_mag[i-1]-2*d_corr_mag[i]+d_corr_mag[i+1]);
          center = nom/denom;
        }
#else
        // Calculates the center of mass between the three points around the peak.
        // Estimate is linear.
        double nom = 0, den = 0;
        nom = d_corr_mag[i-1] + 2*d_corr_mag[i] + 3*d_corr_mag[i+1];
        den = d_corr_mag[i-1] + d_corr_mag[i] + d_corr_mag[i+1];
        double center = nom / den;
        center = (center - 2.0); // adjust for bias in center of mass calculation
#endif

        // Estimated scaling factor for the input stream to normalize
        // the output to +/-1.
        uint32_t maxi;
        volk_32fc_index_max_32u_manual(&maxi, (gr_complex*)in, noutput_items, "generic");
        d_scale = 1 / std::abs(in[maxi]);

        // Calculate the phase offset of the incoming signal.
        //
        // The analytic cross-correlation is:
        //
        // 2A*e_bb(t-t_d)*exp(-j*2*pi*f*(t-t_d) - j*phi_bb(t-t_d) - j*theta_c)
        //

        // The analytic auto-correlation's envelope, e_bb(), has its
        // peak at the "group delay" time, t = t_d.  The analytic
        // cross-correlation's center frequency phase shift, theta_c,
        // is determined from the argument of the analytic
        // cross-correlation at the "group delay" time, t = t_d.
        //
        // Taking the argument of the analytic cross-correlation at
        // any other time will include the baseband auto-correlation's
        // phase term, phi_bb(t-t_d), and a frequency dependent term
        // of the cross-correlation, which I don't believe maps simply
        // to expected symbol phase differences.
        float phase = fast_atan2f(corr[i].imag(), corr[i].real());
        int index = i + d_mark_delay;

        add_item_tag(0, nitems_written(0) + index, pmt::intern("phase_est"),
                     pmt::from_double(phase), d_src_id);
        add_item_tag(0, nitems_written(0) + index, pmt::intern("time_est"),
                     pmt::from_double(center), d_src_id);
        // // N.B. the appropriate d_corr_mag[] index is "i", not "index".
        add_item_tag(0, nitems_written(0) + index, pmt::intern("corr_est"),
                      pmt::from_double(d_corr_mag[i]), d_src_id);
        add_item_tag(0, nitems_written(0) + index, pmt::intern("amp_est"),
                     pmt::from_double(d_scale), d_src_id);

        if (output_items.size() > 1) {
          // N.B. these debug tags are not offset to avoid walking off out buf
          add_item_tag(1, nitems_written(0) + i, pmt::intern("phase_est"),
                       pmt::from_double(phase), d_src_id);
          add_item_tag(1, nitems_written(0) + i, pmt::intern("time_est"),
                       pmt::from_double(center), d_src_id);
          add_item_tag(1, nitems_written(0) + i, pmt::intern("corr_est"),
                       pmt::from_double(d_corr_mag[i]), d_src_id);
          add_item_tag(1, nitems_written(0) + i, pmt::intern("amp_est"),
                       pmt::from_double(d_scale), d_src_id);
        }

        // Skip ahead to the next potential symbol peak
        // (for non-offset/interleaved symbols)
        // Move detection threshold to next sample
        int k = 0;
        for(k=0;k<isps;k++){
            ++i;
           // detection += (d_corr_mag[i+hist_len-1]*d_pfa-d_corr_mag[i-1]*d_pfa)/static_cast<float>(hist_len);
        }
        i+=isps;
      }

      //if (output_items.size() > 1)
      //  add_item_tag(1, nitems_written(0) + noutput_items - 1,
      //               pmt::intern("ce_eow"), pmt::from_uint64(noutput_items),
      //               d_src_id);

      // Delay the output by our correlation filter length so we can
      // tag backwards in time
      memcpy(out, &in[0], sizeof(gr_complex)*noutput_items);

      return noutput_items;
    }

  } /* namespace packetizer */
} /* namespace gr */


/*
Generating: '/home/thomas/gr/gr-packetizer/examples/test_corr_est.py'

Executing: /usr/bin/python2 -u /home/thomas/gr/gr-packetizer/examples/test_corr_est.py

detection threshold: 7631.67
correlated mag: 50680.4
detection threshold: 8032.96
detection threshold: 8614.67
detection threshold: 7996.73
detection threshold: 8355.84
detection threshold: 7570.28
detection threshold: 7811.37
detection threshold: 9660.25
detection threshold: 7976.39
detection threshold: 9408.57
detection threshold: 8414.57
detection threshold: 8650.6
detection threshold: 8058.32
detection threshold: 7724.49
detection threshold: 8682.8
detection threshold: 8718.2
detection threshold: 9041.4
detection threshold: 7944.57
detection threshold: 7781.51
detection threshold: 8556.93
detection threshold: 8082.82
detection threshold: 8641.46
detection threshold: 7118.68
detection threshold: 25.1861
correlated mag: 212.496
detection threshold: 21.0574
detection threshold: 22.8856
detection threshold: 22.4578
correlated mag: 212.641
detection threshold: 21.8651
correlated mag: 213.02
detection threshold: 22.6148
correlated mag: 212.245
detection threshold: 23.5564
detection threshold: 19.8529
detection threshold: 21.9366
correlated mag: 212.226
detection threshold: 25.5764
correlated mag: 216.712
detection threshold: 21.9507
detection threshold: 24.118
detection threshold: 2695.81
correlated mag: 28544.6
detection threshold: 8454.21
detection threshold: 8220.81
detection threshold: 8459.57
detection threshold: 7948.92
detection threshold: 8642.37
detection threshold: 7619.05
detection threshold: 8442.55
detection threshold: 9383.5
detection threshold: 7346.4
detection threshold: 8408.07
detection threshold: 7787.48
detection threshold: 8450.87
detection threshold: 8734.48
detection threshold: 7974.83
detection threshold: 7702.9
detection threshold: 8245.47
detection threshold: 9565.13
detection threshold: 8580.1
detection threshold: 2703.45
correlated mag: 11540.8
detection threshold: 24.3947
detection threshold: 25.3835
detection threshold: 23.9396
detection threshold: 23.9984
detection threshold: 25.3023
detection threshold: 24.0033
detection threshold: 20.3142
detection threshold: 20.9668
*/