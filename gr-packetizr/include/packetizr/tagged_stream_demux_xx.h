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


#ifndef INCLUDED_PACKETIZR_TAGGED_STREAM_DEMUX_XX_H
#define INCLUDED_PACKETIZR_TAGGED_STREAM_DEMUX_XX_H

#include <packetizr/api.h>
#include <gnuradio/tagged_stream_block.h>

namespace gr {
  namespace packetizr {

    /*!
     * \brief <+description of block+>
     * \ingroup packetizr
     *
     */
    class PACKETIZR_API tagged_stream_demux_xx : virtual public gr::tagged_stream_block
    {
     public:
      typedef boost::shared_ptr<tagged_stream_demux_xx> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of packetizr::tagged_stream_demux_xx.
       *
       * To avoid accidental use of raw pointers, packetizr::tagged_stream_demux_xx's
       * constructor is in a private implementation
       * class. packetizr::tagged_stream_demux_xx::make is the public interface for
       * creating new instances.
       */
      static sptr make(size_t itemsize, const std::string &lengthtagname);
    };

  } // namespace packetizr
} // namespace gr

#endif /* INCLUDED_PACKETIZR_TAGGED_STREAM_DEMUX_XX_H */

