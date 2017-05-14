#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Basic Chain Custom2
# Generated: Fri Apr 28 22:33:38 2017
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


class basic_chain_custom2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Basic Chain Custom2")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Basic Chain Custom2")
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

        self.settings = Qt.QSettings("GNU Radio", "basic_chain_custom2")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.preamble = preamble = [1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,1,-1,1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1]
        self.header_formatter = header_formatter = digital.packet_header_default(4, "packet_len", "packet_num", 8)
        self.constel_preamble = constel_preamble = digital.constellation_bpsk()
        self.constel_payload = constel_payload = digital.constellation_bpsk()
        self.constel_header = constel_header = digital.constellation_bpsk()

        self.constel = constel = digital.constellation_calcdist(([1,- 1]), ([0,1]), 2, 1).base()

        self.ber_delay_slider = ber_delay_slider = 0

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_range = Range(1, 256000, 10, 32000, 100)
        self._samp_rate_win = RangeWidget(self._samp_rate_range, self.set_samp_rate, 'Sample rate', "slider", int)
        self.top_grid_layout.addWidget(self._samp_rate_win, 3,1,1,1)
        self._ber_delay_slider_range = Range(0, 10000, 1, 0, 100)
        self._ber_delay_slider_win = RangeWidget(self._ber_delay_slider_range, self.set_ber_delay_slider, 'BER Delay', "slider", int)
        self.top_grid_layout.addWidget(self._ber_delay_slider_win, 4,1,1,2)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	512, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(0, 4)

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
        self.packetizr_tagged_whitener_1 = packetizr.tagged_whitener(False, (), 8, "packet_len")
        self.packetizr_tagged_whitener_0_0 = packetizr.tagged_whitener(False, (), 8, "packet_len")
        self.packetizr_packet_encoder_0 = packetizr.packet_encoder((preamble), constel_header.base(), constel_payload.base(), header_formatter, "packet_len", 100, False, 1)
        self.packetizr_packet_decoder_0 = packetizr.packet_decoder((preamble), constel_header.base(), constel_payload.base(), header_formatter.base(), "packet_len", "front", samp_rate, 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_tagged_stream_0_1 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 4, "packet_len")
        self.blocks_repack_bits_bb_0_1_0 = blocks.repack_bits_bb(8, 8, '', False, gr.GR_LSB_FIRST)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, ber_delay_slider)
        self.blocks_char_to_float_1_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.analog_random_source_x_0_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 1000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0_0, 0), (self.blocks_stream_to_tagged_stream_0_1, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_char_to_float_1_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_1, 1))
        self.connect((self.blocks_repack_bits_bb_0_1_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_1, 0), (self.blocks_repack_bits_bb_0_1_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_1, 0), (self.packetizr_tagged_whitener_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.packetizr_packet_decoder_0, 0))
        self.connect((self.packetizr_packet_decoder_0, 0), (self.packetizr_tagged_whitener_1, 0))
        self.connect((self.packetizr_packet_encoder_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.packetizr_packet_encoder_0, 0), (self.qtgui_time_sink_x_0_2, 0))
        self.connect((self.packetizr_tagged_whitener_0_0, 0), (self.packetizr_packet_encoder_0, 0))
        self.connect((self.packetizr_tagged_whitener_1, 0), (self.blocks_char_to_float_1_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "basic_chain_custom2")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

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

    def get_header_formatter(self):
        return self.header_formatter

    def set_header_formatter(self, header_formatter):
        self.header_formatter = header_formatter

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

    def get_constel(self):
        return self.constel

    def set_constel(self, constel):
        self.constel = constel

    def get_ber_delay_slider(self):
        return self.ber_delay_slider

    def set_ber_delay_slider(self, ber_delay_slider):
        self.ber_delay_slider = ber_delay_slider
        self.blocks_delay_0.set_dly(self.ber_delay_slider)


def main(top_block_cls=basic_chain_custom2, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
