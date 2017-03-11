# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_packetizr_swig', [dirname(__file__)])
        except ImportError:
            import _packetizr_swig
            return _packetizr_swig
        if fp is not None:
            try:
                _mod = imp.load_module('_packetizr_swig', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _packetizr_swig = swig_import_helper()
    del swig_import_helper
else:
    import _packetizr_swig
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr



def high_res_timer_now():
    """high_res_timer_now() -> gr::high_res_timer_type"""
    return _packetizr_swig.high_res_timer_now()

def high_res_timer_now_perfmon():
    """high_res_timer_now_perfmon() -> gr::high_res_timer_type"""
    return _packetizr_swig.high_res_timer_now_perfmon()

def high_res_timer_tps():
    """high_res_timer_tps() -> gr::high_res_timer_type"""
    return _packetizr_swig.high_res_timer_tps()

def high_res_timer_epoch():
    """high_res_timer_epoch() -> gr::high_res_timer_type"""
    return _packetizr_swig.high_res_timer_epoch()
class packet_encoder(object):
    """<+description of block+>"""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def make(sps, preamble, header_constel, payload_constel, itemsize, lengthtagname):
        """
        make(unsigned int sps, int preamble, unsigned int header_constel, unsigned int payload_constel, size_t itemsize, std::string const & lengthtagname) -> packet_encoder_sptr

        Return a shared_ptr to a new instance of packetizr::packet_encoder.

        To avoid accidental use of raw pointers, packetizr::packet_encoder's constructor is in a private implementation class. packetizr::packet_encoder::make is the public interface for creating new instances.

        Params: (sps, preamble, header_constel, payload_constel, itemsize, lengthtagname)
        """
        return _packetizr_swig.packet_encoder_make(sps, preamble, header_constel, payload_constel, itemsize, lengthtagname)

    make = staticmethod(make)
    __swig_destroy__ = _packetizr_swig.delete_packet_encoder
    __del__ = lambda self: None
packet_encoder_swigregister = _packetizr_swig.packet_encoder_swigregister
packet_encoder_swigregister(packet_encoder)

def packet_encoder_make(sps, preamble, header_constel, payload_constel, itemsize, lengthtagname):
    """
    packet_encoder_make(unsigned int sps, int preamble, unsigned int header_constel, unsigned int payload_constel, size_t itemsize, std::string const & lengthtagname) -> packet_encoder_sptr

    Return a shared_ptr to a new instance of packetizr::packet_encoder.

    To avoid accidental use of raw pointers, packetizr::packet_encoder's constructor is in a private implementation class. packetizr::packet_encoder::make is the public interface for creating new instances.

    Params: (sps, preamble, header_constel, payload_constel, itemsize, lengthtagname)
    """
    return _packetizr_swig.packet_encoder_make(sps, preamble, header_constel, payload_constel, itemsize, lengthtagname)

class packet_encoder_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::packetizr::packet_encoder)> class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(boost::shared_ptr<(gr::packetizr::packet_encoder)> self) -> packet_encoder_sptr
        __init__(boost::shared_ptr<(gr::packetizr::packet_encoder)> self, packet_encoder p) -> packet_encoder_sptr
        """
        this = _packetizr_swig.new_packet_encoder_sptr(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def __deref__(self):
        """__deref__(packet_encoder_sptr self) -> packet_encoder"""
        return _packetizr_swig.packet_encoder_sptr___deref__(self)

    __swig_destroy__ = _packetizr_swig.delete_packet_encoder_sptr
    __del__ = lambda self: None

    def make(self, sps, preamble, header_constel, payload_constel, itemsize, lengthtagname):
        """
        make(packet_encoder_sptr self, unsigned int sps, int preamble, unsigned int header_constel, unsigned int payload_constel, size_t itemsize, std::string const & lengthtagname) -> packet_encoder_sptr

        Return a shared_ptr to a new instance of packetizr::packet_encoder.

        To avoid accidental use of raw pointers, packetizr::packet_encoder's constructor is in a private implementation class. packetizr::packet_encoder::make is the public interface for creating new instances.

        Params: (sps, preamble, header_constel, payload_constel, itemsize, lengthtagname)
        """
        return _packetizr_swig.packet_encoder_sptr_make(self, sps, preamble, header_constel, payload_constel, itemsize, lengthtagname)


    def history(self):
        """history(packet_encoder_sptr self) -> unsigned int"""
        return _packetizr_swig.packet_encoder_sptr_history(self)


    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(packet_encoder_sptr self, int which, int delay)
        declare_sample_delay(packet_encoder_sptr self, unsigned int delay)
        """
        return _packetizr_swig.packet_encoder_sptr_declare_sample_delay(self, *args)


    def sample_delay(self, which):
        """sample_delay(packet_encoder_sptr self, int which) -> unsigned int"""
        return _packetizr_swig.packet_encoder_sptr_sample_delay(self, which)


    def output_multiple(self):
        """output_multiple(packet_encoder_sptr self) -> int"""
        return _packetizr_swig.packet_encoder_sptr_output_multiple(self)


    def relative_rate(self):
        """relative_rate(packet_encoder_sptr self) -> double"""
        return _packetizr_swig.packet_encoder_sptr_relative_rate(self)


    def start(self):
        """start(packet_encoder_sptr self) -> bool"""
        return _packetizr_swig.packet_encoder_sptr_start(self)


    def stop(self):
        """stop(packet_encoder_sptr self) -> bool"""
        return _packetizr_swig.packet_encoder_sptr_stop(self)


    def nitems_read(self, which_input):
        """nitems_read(packet_encoder_sptr self, unsigned int which_input) -> uint64_t"""
        return _packetizr_swig.packet_encoder_sptr_nitems_read(self, which_input)


    def nitems_written(self, which_output):
        """nitems_written(packet_encoder_sptr self, unsigned int which_output) -> uint64_t"""
        return _packetizr_swig.packet_encoder_sptr_nitems_written(self, which_output)


    def max_noutput_items(self):
        """max_noutput_items(packet_encoder_sptr self) -> int"""
        return _packetizr_swig.packet_encoder_sptr_max_noutput_items(self)


    def set_max_noutput_items(self, m):
        """set_max_noutput_items(packet_encoder_sptr self, int m)"""
        return _packetizr_swig.packet_encoder_sptr_set_max_noutput_items(self, m)


    def unset_max_noutput_items(self):
        """unset_max_noutput_items(packet_encoder_sptr self)"""
        return _packetizr_swig.packet_encoder_sptr_unset_max_noutput_items(self)


    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(packet_encoder_sptr self) -> bool"""
        return _packetizr_swig.packet_encoder_sptr_is_set_max_noutput_items(self)


    def set_min_noutput_items(self, m):
        """set_min_noutput_items(packet_encoder_sptr self, int m)"""
        return _packetizr_swig.packet_encoder_sptr_set_min_noutput_items(self, m)


    def min_noutput_items(self):
        """min_noutput_items(packet_encoder_sptr self) -> int"""
        return _packetizr_swig.packet_encoder_sptr_min_noutput_items(self)


    def max_output_buffer(self, i):
        """max_output_buffer(packet_encoder_sptr self, int i) -> long"""
        return _packetizr_swig.packet_encoder_sptr_max_output_buffer(self, i)


    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(packet_encoder_sptr self, long max_output_buffer)
        set_max_output_buffer(packet_encoder_sptr self, int port, long max_output_buffer)
        """
        return _packetizr_swig.packet_encoder_sptr_set_max_output_buffer(self, *args)


    def min_output_buffer(self, i):
        """min_output_buffer(packet_encoder_sptr self, int i) -> long"""
        return _packetizr_swig.packet_encoder_sptr_min_output_buffer(self, i)


    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(packet_encoder_sptr self, long min_output_buffer)
        set_min_output_buffer(packet_encoder_sptr self, int port, long min_output_buffer)
        """
        return _packetizr_swig.packet_encoder_sptr_set_min_output_buffer(self, *args)


    def pc_noutput_items(self):
        """pc_noutput_items(packet_encoder_sptr self) -> float"""
        return _packetizr_swig.packet_encoder_sptr_pc_noutput_items(self)


    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(packet_encoder_sptr self) -> float"""
        return _packetizr_swig.packet_encoder_sptr_pc_noutput_items_avg(self)


    def pc_noutput_items_var(self):
        """pc_noutput_items_var(packet_encoder_sptr self) -> float"""
        return _packetizr_swig.packet_encoder_sptr_pc_noutput_items_var(self)


    def pc_nproduced(self):
        """pc_nproduced(packet_encoder_sptr self) -> float"""
        return _packetizr_swig.packet_encoder_sptr_pc_nproduced(self)


    def pc_nproduced_avg(self):
        """pc_nproduced_avg(packet_encoder_sptr self) -> float"""
        return _packetizr_swig.packet_encoder_sptr_pc_nproduced_avg(self)


    def pc_nproduced_var(self):
        """pc_nproduced_var(packet_encoder_sptr self) -> float"""
        return _packetizr_swig.packet_encoder_sptr_pc_nproduced_var(self)


    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(packet_encoder_sptr self, int which) -> float
        pc_input_buffers_full(packet_encoder_sptr self) -> pmt_vector_float
        """
        return _packetizr_swig.packet_encoder_sptr_pc_input_buffers_full(self, *args)


    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(packet_encoder_sptr self, int which) -> float
        pc_input_buffers_full_avg(packet_encoder_sptr self) -> pmt_vector_float
        """
        return _packetizr_swig.packet_encoder_sptr_pc_input_buffers_full_avg(self, *args)


    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(packet_encoder_sptr self, int which) -> float
        pc_input_buffers_full_var(packet_encoder_sptr self) -> pmt_vector_float
        """
        return _packetizr_swig.packet_encoder_sptr_pc_input_buffers_full_var(self, *args)


    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(packet_encoder_sptr self, int which) -> float
        pc_output_buffers_full(packet_encoder_sptr self) -> pmt_vector_float
        """
        return _packetizr_swig.packet_encoder_sptr_pc_output_buffers_full(self, *args)


    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(packet_encoder_sptr self, int which) -> float
        pc_output_buffers_full_avg(packet_encoder_sptr self) -> pmt_vector_float
        """
        return _packetizr_swig.packet_encoder_sptr_pc_output_buffers_full_avg(self, *args)


    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(packet_encoder_sptr self, int which) -> float
        pc_output_buffers_full_var(packet_encoder_sptr self) -> pmt_vector_float
        """
        return _packetizr_swig.packet_encoder_sptr_pc_output_buffers_full_var(self, *args)


    def pc_work_time(self):
        """pc_work_time(packet_encoder_sptr self) -> float"""
        return _packetizr_swig.packet_encoder_sptr_pc_work_time(self)


    def pc_work_time_avg(self):
        """pc_work_time_avg(packet_encoder_sptr self) -> float"""
        return _packetizr_swig.packet_encoder_sptr_pc_work_time_avg(self)


    def pc_work_time_var(self):
        """pc_work_time_var(packet_encoder_sptr self) -> float"""
        return _packetizr_swig.packet_encoder_sptr_pc_work_time_var(self)


    def pc_work_time_total(self):
        """pc_work_time_total(packet_encoder_sptr self) -> float"""
        return _packetizr_swig.packet_encoder_sptr_pc_work_time_total(self)


    def pc_throughput_avg(self):
        """pc_throughput_avg(packet_encoder_sptr self) -> float"""
        return _packetizr_swig.packet_encoder_sptr_pc_throughput_avg(self)


    def set_processor_affinity(self, mask):
        """set_processor_affinity(packet_encoder_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _packetizr_swig.packet_encoder_sptr_set_processor_affinity(self, mask)


    def unset_processor_affinity(self):
        """unset_processor_affinity(packet_encoder_sptr self)"""
        return _packetizr_swig.packet_encoder_sptr_unset_processor_affinity(self)


    def processor_affinity(self):
        """processor_affinity(packet_encoder_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _packetizr_swig.packet_encoder_sptr_processor_affinity(self)


    def active_thread_priority(self):
        """active_thread_priority(packet_encoder_sptr self) -> int"""
        return _packetizr_swig.packet_encoder_sptr_active_thread_priority(self)


    def thread_priority(self):
        """thread_priority(packet_encoder_sptr self) -> int"""
        return _packetizr_swig.packet_encoder_sptr_thread_priority(self)


    def set_thread_priority(self, priority):
        """set_thread_priority(packet_encoder_sptr self, int priority) -> int"""
        return _packetizr_swig.packet_encoder_sptr_set_thread_priority(self, priority)


    def name(self):
        """name(packet_encoder_sptr self) -> std::string"""
        return _packetizr_swig.packet_encoder_sptr_name(self)


    def symbol_name(self):
        """symbol_name(packet_encoder_sptr self) -> std::string"""
        return _packetizr_swig.packet_encoder_sptr_symbol_name(self)


    def input_signature(self):
        """input_signature(packet_encoder_sptr self) -> io_signature_sptr"""
        return _packetizr_swig.packet_encoder_sptr_input_signature(self)


    def output_signature(self):
        """output_signature(packet_encoder_sptr self) -> io_signature_sptr"""
        return _packetizr_swig.packet_encoder_sptr_output_signature(self)


    def unique_id(self):
        """unique_id(packet_encoder_sptr self) -> long"""
        return _packetizr_swig.packet_encoder_sptr_unique_id(self)


    def to_basic_block(self):
        """to_basic_block(packet_encoder_sptr self) -> basic_block_sptr"""
        return _packetizr_swig.packet_encoder_sptr_to_basic_block(self)


    def check_topology(self, ninputs, noutputs):
        """check_topology(packet_encoder_sptr self, int ninputs, int noutputs) -> bool"""
        return _packetizr_swig.packet_encoder_sptr_check_topology(self, ninputs, noutputs)


    def alias(self):
        """alias(packet_encoder_sptr self) -> std::string"""
        return _packetizr_swig.packet_encoder_sptr_alias(self)


    def set_block_alias(self, name):
        """set_block_alias(packet_encoder_sptr self, std::string name)"""
        return _packetizr_swig.packet_encoder_sptr_set_block_alias(self, name)


    def _post(self, which_port, msg):
        """_post(packet_encoder_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _packetizr_swig.packet_encoder_sptr__post(self, which_port, msg)


    def message_ports_in(self):
        """message_ports_in(packet_encoder_sptr self) -> swig_int_ptr"""
        return _packetizr_swig.packet_encoder_sptr_message_ports_in(self)


    def message_ports_out(self):
        """message_ports_out(packet_encoder_sptr self) -> swig_int_ptr"""
        return _packetizr_swig.packet_encoder_sptr_message_ports_out(self)


    def message_subscribers(self, which_port):
        """message_subscribers(packet_encoder_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _packetizr_swig.packet_encoder_sptr_message_subscribers(self, which_port)

packet_encoder_sptr_swigregister = _packetizr_swig.packet_encoder_sptr_swigregister
packet_encoder_sptr_swigregister(packet_encoder_sptr)


packet_encoder_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
packet_encoder = packet_encoder.make;


