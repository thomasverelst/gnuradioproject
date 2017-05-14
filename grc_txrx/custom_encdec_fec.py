#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Custom Encdec Fec
# Generated: Sun Apr 30 01:40:30 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy
import packetizr
import sip
import sys
from gnuradio import qtgui


class custom_encdec_fec(gr.top_block, Qt.QWidget):

    def __init__(self, frame_size=60, puncpat='11'):
        gr.top_block.__init__(self, "Custom Encdec Fec")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Custom Encdec Fec")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "custom_encdec_fec")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.frame_size = frame_size
        self.puncpat = puncpat

        ##################################################
        # Variables
        ##################################################
        self.rate = rate = 2
        self.polys = polys = [109, 79]
        self.k = k = 7
        self.samp_rate = samp_rate = 32000
        self.preamble = preamble = [1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,1,-1,1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1]
        self.packlen = packlen = 4
        self.header_formatter = header_formatter = digital.packet_header_default(4, "packet_len", "packet_num", 8)


        self.enc_cc = enc_cc = fec.cc_encoder_make(frame_size*8, k, rate, (polys), 0, fec.CC_STREAMING, False)



        self.dec_cc = dec_cc = fec.cc_decoder.make(frame_size*8, k, rate, (polys), 0, -1, fec.CC_STREAMING, False)

        self.constel_preamble = constel_preamble = digital.constellation_bpsk()
        self.constel_payload = constel_payload = digital.constellation_bpsk()
        self.constel_header = constel_header = digital.constellation_bpsk()

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_range = Range(1, 256000, 10, 32000, 100)
        self._samp_rate_win = RangeWidget(self._samp_rate_range, self.set_samp_rate, 'Sample rate', "slider", int)
        self.top_layout.addWidget(self._samp_rate_win)
        self._packlen_range = Range(1, 4096, 1, 4, 100)
        self._packlen_win = RangeWidget(self._packlen_range, self.set_packlen, 'Packet Length', "slider", int)
        self.top_layout.addWidget(self._packlen_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	512, #size
        	samp_rate, #samp_rate
        	"Input/Output comparison", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(0, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

        labels = ['Original data', 'Received data', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0_2 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"TX Symbol Stream", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_2.set_update_time(0.10)
        self.qtgui_time_sink_x_0_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_2.enable_autoscale(False)
        self.qtgui_time_sink_x_0_2.enable_grid(False)
        self.qtgui_time_sink_x_0_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_2.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_2.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_2.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_2.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_2_win = sip.wrapinstance(self.qtgui_time_sink_x_0_2.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_2_win)
        self.packetizr_packet_encoder_0 = packetizr.packet_encoder((preamble), constel_header.base(), constel_payload.base(), header_formatter, "packet_len", 100, False, 1)
        self.packetizr_packet_decoder_0 = packetizr.packet_decoder((preamble), constel_header.base(), constel_payload.base(), header_formatter.base(), "packet_len", False, False, False, samp_rate, 1)
        self.fec_extended_tagged_encoder_0_0 = fec.extended_tagged_encoder(encoder_obj_list=enc_cc, puncpat='11', lentagname="packet_len", mtu=1500)
        self.fec_extended_tagged_decoder_0_0 = self.fec_extended_tagged_decoder_0_0 = fec_extended_tagged_decoder_0_0 = fec.extended_tagged_decoder(decoder_obj_list=dec_cc, ann=None, puncpat='11', integration_period=10000, lentagname="packet_len", mtu=1500)
        self.digital_map_bb_0 = digital.map_bb(([-1,1]))
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_tagged_stream_0_1 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, packlen, "packet_len")
        self.blocks_repack_bits_bb_0_0_1 = blocks.repack_bits_bb(8, 1, "packet_len", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0_0_0 = blocks.repack_bits_bb(1, 8, "packet_len", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, 1, "packet_len", False, gr.GR_LSB_FIRST)
        self.blocks_char_to_float_1_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_1_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_1_0_0 = blocks.char_to_float(1, 1)
        self.analog_random_source_x_0_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 1000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0_0, 0), (self.blocks_stream_to_tagged_stream_0_1, 0))
        self.connect((self.blocks_char_to_float_1_0_0, 0), (self.qtgui_time_sink_x_1, 1))
        self.connect((self.blocks_char_to_float_1_0_0_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_char_to_float_1_1, 0), (self.fec_extended_tagged_decoder_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.blocks_char_to_float_1_0_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.fec_extended_tagged_encoder_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_0, 0), (self.packetizr_packet_encoder_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0_1, 0), (self.digital_map_bb_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_1, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.packetizr_packet_decoder_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.blocks_char_to_float_1_1, 0))
        self.connect((self.fec_extended_tagged_decoder_0_0, 0), (self.blocks_char_to_float_1_0_0, 0))
        self.connect((self.fec_extended_tagged_encoder_0_0, 0), (self.blocks_repack_bits_bb_0_0_0, 0))
        self.connect((self.packetizr_packet_decoder_0, 0), (self.blocks_repack_bits_bb_0_0_1, 0))
        self.connect((self.packetizr_packet_encoder_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.packetizr_packet_encoder_0, 0), (self.qtgui_time_sink_x_0_2, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "custom_encdec_fec")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_frame_size(self):
        return self.frame_size

    def set_frame_size(self, frame_size):
        self.frame_size = frame_size

    def get_puncpat(self):
        return self.puncpat

    def set_puncpat(self, puncpat):
        self.puncpat = puncpat

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate

    def get_polys(self):
        return self.polys

    def set_polys(self, polys):
        self.polys = polys

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_2.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_preamble(self):
        return self.preamble

    def set_preamble(self, preamble):
        self.preamble = preamble

    def get_packlen(self):
        return self.packlen

    def set_packlen(self, packlen):
        self.packlen = packlen
        self.blocks_stream_to_tagged_stream_0_1.set_packet_len(self.packlen)
        self.blocks_stream_to_tagged_stream_0_1.set_packet_len_pmt(self.packlen)

    def get_header_formatter(self):
        return self.header_formatter

    def set_header_formatter(self, header_formatter):
        self.header_formatter = header_formatter

    def get_enc_cc(self):
        return self.enc_cc

    def set_enc_cc(self, enc_cc):
        self.enc_cc = enc_cc

    def get_dec_cc(self):
        return self.dec_cc

    def set_dec_cc(self, dec_cc):
        self.dec_cc = dec_cc

    def get_constel_preamble(self):
        return self.constel_preamble

    def set_constel_preamble(self, constel_preamble):
        self.constel_preamble = constel_preamble

    def get_constel_payload(self):
        return self.constel_payload

    def set_constel_payload(self, constel_payload):
        self.constel_payload = constel_payload

    def get_constel_header(self):
        return self.constel_header

    def set_constel_header(self, constel_header):
        self.constel_header = constel_header


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--frame-size", dest="frame_size", type="intx", default=60,
        help="Set Frame Size [default=%default]")
    parser.add_option(
        "", "--puncpat", dest="puncpat", type="string", default='11',
        help="Set puncpat [default=%default]")
    return parser


def main(top_block_cls=custom_encdec_fec, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(frame_size=options.frame_size, puncpat=options.puncpat)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
