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


#ifndef INCLUDED_TEST_TEST_H
#define INCLUDED_TEST_TEST_H

#include <test/api.h>
#include <gnuradio/tagged_stream_block.h>

namespace gr {
  namespace test {

    /*!
     * \brief <+description of block+>
     * \ingroup test
     *
     */
    class TEST_API test : virtual public gr::tagged_stream_block
    {
     public:
      typedef boost::shared_ptr<test> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of test::test.
       *
       * To avoid accidental use of raw pointers, test::test's
       * constructor is in a private implementation
       * class. test::test::make is the public interface for
       * creating new instances.
       */
      static sptr make(unsigned int sps, int preamble, digital::constellation_sptr header_constel, digital::constellation_sptr payload_constel, size_t itemsize, const std::string &lengthtagname);
    };

  } // namespace test
} // namespace gr

#endif /* INCLUDED_TEST_TEST_H */

