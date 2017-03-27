
/*
 * This file was automatically generated using swig_doc.py.
 *
 * Any changes to it will be lost next time it is regenerated.
 */




%feature("docstring") gr::packetizr::packet_encoder "<+description of block+>"

%feature("docstring") gr::packetizr::packet_encoder::make "Return a shared_ptr to a new instance of packetizr::packet_encoder.

To avoid accidental use of raw pointers, packetizr::packet_encoder's constructor is in a private implementation class. packetizr::packet_encoder::make is the public interface for creating new instances.

Params: (preamble, constel_header, constel_payload, header_formatter, lengthtagname, itemsize)"