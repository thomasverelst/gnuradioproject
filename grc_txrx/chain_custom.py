#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Chain Custom
# Generated: Sun May 21 17:07:05 2017
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy
import packetizer
import sip
import sys
from gnuradio import qtgui


class chain_custom(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Chain Custom")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Chain Custom")
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

        self.settings = Qt.QSettings("GNU Radio", "chain_custom")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.eb = eb = 0.35
        self.rrc_taps_enc = rrc_taps_enc = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 11*sps*nfilts)
        self.rxshape = rxshape = filter.pfb_arb_resampler_ccf(sps,  rrc_taps_enc , 32)
        self.preamble = preamble = [1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,1,-1,1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1]
        self.constel_header = constel_header = digital.constellation_bpsk()
        self.time_offset = time_offset = 1
        self.shaped_preamble = shaped_preamble = packetizer.pulseshape_vector(rxshape .to_basic_block(), preamble)
        self.samp_rate = samp_rate = 32000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), eb, 5*sps*nfilts)
        self.noise = noise = 0.1
        self.matched_filter = matched_filter = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 11*sps*nfilts)
        self.header_formatter = header_formatter = digital.packet_header_default(32/constel_header.bits_per_symbol(), "packet_len", "packet_num", constel_header.bits_per_symbol())
        self.freq_offset = freq_offset = 0
        self.constel_preamble = constel_preamble = digital.constellation_bpsk()
        self.constel_payload = constel_payload = digital.constellation_qpsk()

        ##################################################
        # Blocks
        ##################################################
        self._time_offset_range = Range(0.995, 1.005, 0.00001, 1, 200)
        self._time_offset_win = RangeWidget(self._time_offset_range, self.set_time_offset, 'Timing Offset', "slider", float)
        self.top_grid_layout.addWidget(self._time_offset_win, 0,2,1,1)
        self._samp_rate_range = Range(1, 256000, 10, 32000, 100)
        self._samp_rate_win = RangeWidget(self._samp_rate_range, self.set_samp_rate, 'Sample rate', "slider", int)
        self.top_grid_layout.addWidget(self._samp_rate_win, 0,0,1,1)
        self._noise_range = Range(0, 1, 0.005, 0.1, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, 'Noise', "slider", float)
        self.top_grid_layout.addWidget(self._noise_win, 0,1,1,1)
        self._freq_offset_range = Range(-0.001, 0.001, 0.00002, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, 'Frequency Offset', "slider", float)
        self.top_grid_layout.addWidget(self._freq_offset_win, 0,3,1,1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	512, #size
        	samp_rate, #samp_rate
        	"In/out comparison", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

        labels = ["Source data", "Soft decoded data", "Hard decoded data", '', '',
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_win, 3,0,1,4)
        self.qtgui_time_sink_x_0_1_0_0_2_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"RX  Polyphased Stream", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0_0_2_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0_0_2_0.set_y_axis(-4, 4)

        self.qtgui_time_sink_x_0_1_0_0_2_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_0_0_2_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0_0_2_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "packet_len")
        self.qtgui_time_sink_x_0_1_0_0_2_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_0_0_2_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0_0_2_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0_0_2_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_1_0_0_2_0.disable_legend()

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
                    self.qtgui_time_sink_x_0_1_0_0_2_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_1_0_0_2_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_1_0_0_2_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0_0_2_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0_0_2_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0_0_2_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0_0_2_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0_0_2_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_0_2_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0_0_2_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_1_0_0_2_0_win, 5,0,1,2)
        self.qtgui_time_sink_x_0_1_0_0_0_0_0 = qtgui.time_sink_c(
        	5000, #size
        	samp_rate, #samp_rate
        	"RX Correlated Stream", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_0_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "corr_est")
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_1_0_0_0_0_0.disable_legend()

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
                    self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_1_0_0_0_0_0_win, 4,2,1,2)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	512, #size
        	samp_rate, #samp_rate
        	"TX Symbols", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, False)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

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
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 4,0,1,2)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(rrc_taps_enc),
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(40)

        self.packetizer_packet_encoder_0 = packetizer.packet_encoder((preamble), constel_header.base(), constel_payload.base(), header_formatter.base(), "packet_len", 100, False, 1)
        self.packetizer_packet_decoder_0 = packetizer.packet_decoder((preamble), constel_header.base(), constel_payload.base(), header_formatter.base(), "corr_est", True, False, False, samp_rate, 1)
        self.packetizer_message_order_check_0 = packetizer.message_order_check("packet_num")
        self.packetizer_corr_est_cc_0 = packetizer.corr_est_cc((shaped_preamble), 4, 100, 0.9999996, 0.96)
        self.digital_pfb_clock_sync_xxx_0_0_0 = digital.pfb_clock_sync_ccf(sps, 3.14*2/100, (rrc_taps), 32, 0, 1.5, 1)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise,
        	frequency_offset=freq_offset,
        	epsilon=time_offset,
        	taps=(1.0, ),
        	noise_seed=0,
        	block_tags=True
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 100, "packet_len")
        self.blocks_repack_bits_bb_0_1 = blocks.repack_bits_bb(8, 1, '', False, gr.GR_LSB_FIRST)
        self.blocks_char_to_float_1_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 10)), True)
        self.analog_agc2_xx_0_0_0 = analog.agc2_cc(1e-3, 1e-4, 1.0, 1.0)
        self.analog_agc2_xx_0_0_0.set_max_gain(5)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.packetizer_packet_decoder_0, 'header_data'), (self.packetizer_message_order_check_0, 'data'))
        self.connect((self.analog_agc2_xx_0_0_0, 0), (self.packetizer_corr_est_cc_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_repack_bits_bb_0_1, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_char_to_float_1_0, 0), (self.qtgui_time_sink_x_1, 1))
        self.connect((self.blocks_repack_bits_bb_0_1, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.packetizer_packet_encoder_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.analog_agc2_xx_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_0, 0), (self.packetizer_packet_decoder_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0_0, 0), (self.qtgui_time_sink_x_0_1_0_0_2_0, 0))
        self.connect((self.packetizer_corr_est_cc_0, 0), (self.digital_pfb_clock_sync_xxx_0_0_0, 0))
        self.connect((self.packetizer_corr_est_cc_0, 0), (self.qtgui_time_sink_x_0_1_0_0_0_0_0, 0))
        self.connect((self.packetizer_packet_decoder_0, 0), (self.blocks_char_to_float_1_0, 0))
        self.connect((self.packetizer_packet_encoder_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.packetizer_packet_encoder_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_throttle_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "chain_custom")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps_enc(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, 11*self.sps*self.nfilts))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.eb, 5*self.sps*self.nfilts))
        self.set_rxshape(filter.pfb_arb_resampler_ccf(self.sps,  self.rrc_taps_enc , 32) )
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)
        self.set_matched_filter(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, 11*self.sps*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps_enc(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, 11*self.sps*self.nfilts))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.eb, 5*self.sps*self.nfilts))
        self.set_matched_filter(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, 11*self.sps*self.nfilts))

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.set_rrc_taps_enc(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, 11*self.sps*self.nfilts))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.eb, 5*self.sps*self.nfilts))
        self.set_matched_filter(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, 11*self.sps*self.nfilts))

    def get_rrc_taps_enc(self):
        return self.rrc_taps_enc

    def set_rrc_taps_enc(self, rrc_taps_enc):
        self.rrc_taps_enc = rrc_taps_enc
        self.set_rxshape(filter.pfb_arb_resampler_ccf(self.sps,  self.rrc_taps_enc , 32) )
        self.pfb_arb_resampler_xxx_0.set_taps((self.rrc_taps_enc))

    def get_rxshape(self):
        return self.rxshape

    def set_rxshape(self, rxshape):
        self.rxshape = rxshape

    def get_preamble(self):
        return self.preamble

    def set_preamble(self, preamble):
        self.preamble = preamble

    def get_constel_header(self):
        return self.constel_header

    def set_constel_header(self, constel_header):
        self.constel_header = constel_header

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset
        self.channels_channel_model_0.set_timing_offset(self.time_offset)

    def get_shaped_preamble(self):
        return self.shaped_preamble

    def set_shaped_preamble(self, shaped_preamble):
        self.shaped_preamble = shaped_preamble

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1_0_0_2_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0_0_0.update_taps((self.rrc_taps))

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.channels_channel_model_0.set_noise_voltage(self.noise)

    def get_matched_filter(self):
        return self.matched_filter

    def set_matched_filter(self, matched_filter):
        self.matched_filter = matched_filter

    def get_header_formatter(self):
        return self.header_formatter

    def set_header_formatter(self, header_formatter):
        self.header_formatter = header_formatter

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.channels_channel_model_0.set_frequency_offset(self.freq_offset)

    def get_constel_preamble(self):
        return self.constel_preamble

    def set_constel_preamble(self, constel_preamble):
        self.constel_preamble = constel_preamble

    def get_constel_payload(self):
        return self.constel_payload

    def set_constel_payload(self, constel_payload):
        self.constel_payload = constel_payload


def main(top_block_cls=chain_custom, options=None):

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
