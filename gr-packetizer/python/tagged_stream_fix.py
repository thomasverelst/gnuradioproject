#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 Thomas Verelst
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
from gnuradio import digital
from gnuradio import blocks
import pmt

class tagged_stream_fix(gr.basic_block):
    """
    Tagged Stream Fix:

    fixes a stream where the packet length does not correspond to the number of samples. 
    For example, if we have a stream with a packet length tag with value 50, and between each tag there are 52 samples,
    the block will remove the last 2 samples from the output stream to make a stream
    with packet length tag of 50 and 50 samples between each tag.

    Tagged_stream blocks cannot handle "unbalanced" streams (more samples between packets than the packet length indicates), so 
    this block will "fix" the stream.
    """
    def __init__(self, tagname, itemsize):
        gr.basic_block.__init__(self,
            name="tagged_stream_fix",
            in_sig=[itemsize],
            out_sig=[itemsize])
        self.todo = 0; #how many samples from last frame that should be outputted
        self.n_consumed = 0;
        self.tagname = tagname
        self.set_tag_propagation_policy(0)

    def forecast(self, noutput_items, ninput_items_required):
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):
        debug = False

        output_len = len(output_items[0])
        input_len = len(input_items[0])
        self.n_consumed = 0;
        if(debug):
            print "START", self.todo, input_len, output_len

        #first process the todo samples that were carried over from last call
        i_in = min(self.todo, min(input_len, output_len))
        i_out = i_in
        
        output_items[0][0:i_out] = input_items[0][0:i_in]
        self.todo -= i_in
        self.n_consumed += i_in;

        #if all todo samples have been processsed now and we can handle some more samples
        if self.todo == 0 and i_out < output_len:

            #process new incoming tags
            tags = self.get_tags_in_window(0, 0, input_len)

           
            for tag in tags:
                ptag = gr.tag_to_python(tag)

                if(ptag.key == self.tagname):

                    rel_start = ptag.offset - self.nitems_read(0);
                    if debug:
                        print "PROCESS", rel_start, input_len, i_out, output_len
                    
                    if rel_start>= input_len:
                        self.n_consumed = input_len
                        break
                    
                    self.add_item_tag(0, self.nitems_written(0)+i_out, pmt.string_to_symbol(ptag.key),  pmt.from_long(ptag.value))

                    if rel_start + ptag.value >= input_len or i_out + ptag.value >= output_len:
                        # Full packet not in range for output or input, process the next part to next call
                        k_in = min(input_len-rel_start ,  output_len-i_out)
                        output_items[0][i_out:i_out+k_in] = input_items[0][rel_start:rel_start + k_in]
                        i_out += k_in;
                            
                        self.todo = ptag.value - k_in
                        self.n_consumed = rel_start + k_in;
                      
                        if(debug):
                            print "End of input or output buffer. Carry over ",self.todo

                        break
                    else:
                        # We can process the full packet at once 
                        output_items[0][i_out:i_out+ptag.value] = input_items[0][rel_start:rel_start+ptag.value]
                        i_out += ptag.value;
                        self.n_consumed = rel_start + ptag.value;
                        

                        #if output buffer is full now
                        if i_out >= output_len:
                            if(debug):
                                print "End of output buffer"
                            break
    

        if(debug):
            print "CONSUME" , self.n_consumed
        self.consume_each(self.n_consumed)
        return i_out
