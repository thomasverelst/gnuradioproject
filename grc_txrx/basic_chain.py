#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Basic Chain
# Generated: Sat Mar 25 19:54:27 2017
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
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy
import sip
import sys


class basic_chain(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Basic Chain")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Basic Chain")
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

        self.settings = Qt.QSettings("GNU Radio", "basic_chain")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.eb = eb = 0.35
        self.constel_header = constel_header = digital.constellation_bpsk()
        self.samp_rate = samp_rate = 32000
        self.rrc_taps_enc = rrc_taps_enc = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 11*sps*nfilts)
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), eb, 5*sps*nfilts)
        self.preamble = preamble = [1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,1,-1,1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1]
        self.matched_filter = matched_filter = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 11*sps*nfilts)
        self.header_formatter = header_formatter = digital.packet_header_default(4, "packet_len", "packet_num", constel_header.bits_per_symbol())
        self.constel_preamble = constel_preamble = digital.constellation_bpsk()
        self.constel_payload = constel_payload = digital.constellation_bpsk()

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_range = Range(1, 256000, 10, 32000, 200)
        self._samp_rate_win = RangeWidget(self._samp_rate_range, self.set_samp_rate, "Sample rate", "slider", int)
        self.top_grid_layout.addWidget(self._samp_rate_win, 3,1,1,1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Data comparison", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1.disable_legend()
        
        labels = ["Original data", "Received data", "", "", "",
                  "", "", "", "", ""]
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
        self.qtgui_time_sink_x_0_3 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"TX Symbols", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_3.set_update_time(0.10)
        self.qtgui_time_sink_x_0_3.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_3.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_3.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_3.enable_autoscale(False)
        self.qtgui_time_sink_x_0_3.enable_grid(False)
        self.qtgui_time_sink_x_0_3.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_3.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_3.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_3.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_3.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_3.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_3.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_3.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_3.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_3.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_3_win = sip.wrapinstance(self.qtgui_time_sink_x_0_3.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_3_win)
        self.qtgui_time_sink_x_0_2 = qtgui.time_sink_f(
        	10000, #size
        	samp_rate*2, #samp_rate
        	"Correlation", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_2.set_update_time(0.02)
        self.qtgui_time_sink_x_0_2.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_2.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_2.enable_autoscale(False)
        self.qtgui_time_sink_x_0_2.enable_grid(False)
        self.qtgui_time_sink_x_0_2.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_2.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
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
                self.qtgui_time_sink_x_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_2.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_2_win = sip.wrapinstance(self.qtgui_time_sink_x_0_2.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_2_win)
        self.qtgui_time_sink_x_0_1_0_0_2 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"RX  Polyphased Stream", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0_0_2.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0_0_2.set_y_axis(-100, 100)
        
        self.qtgui_time_sink_x_0_1_0_0_2.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_1_0_0_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0_0_2.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_0_0_2.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0_0_2.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_1_0_0_2.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_1_0_0_2.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_1_0_0_2.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_1_0_0_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0_0_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0_0_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0_0_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0_0_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0_0_2.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_1_0_0_2_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0_0_2.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_0_0_2_win)
        self.qtgui_time_sink_x_0_1_0_0_1_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"RX  Demux Paylaod Stream", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0_0_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0_0_1_0.set_y_axis(-100, 100)
        
        self.qtgui_time_sink_x_0_1_0_0_1_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_1_0_0_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0_0_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_0_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0_0_1_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_1_0_0_1_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_1_0_0_1_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_1_0_0_1_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_1_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0_0_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_1_0_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_0_0_1_0_win)
        self.qtgui_time_sink_x_0_1_0_0_1 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"RX  Demux Header Stream", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0_0_1.set_y_axis(-100, 100)
        
        self.qtgui_time_sink_x_0_1_0_0_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_1_0_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0_0_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_1_0_0_1.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_1_0_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_1_0_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_1_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_1_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_0_0_1_win)
        self.qtgui_time_sink_x_0_1_0_0_0_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"RX Correlated Stream", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0_0_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_1_0_0_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_1_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0_0_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_1_0_0_0_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_1_0_0_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_1_0_0_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_1_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_1_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_0_0_0_0_win)
        self.qtgui_time_sink_x_0_1_0_0_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"RX AGC Stream", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_1_0_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_1_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_1_0_0_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_1_0_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_1_0_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_1_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_0_0_0_win)
        self.qtgui_time_sink_x_0_1_0_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"RX  Costas Stream", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0_0.set_y_axis(-100, 100)
        
        self.qtgui_time_sink_x_0_1_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_1_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_1_0_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_1_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_1_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_0_0_win)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"TX  Stream", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"RX Symbols", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
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
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"RX  Header Constellations", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_win)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(rrc_taps_enc),
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)
        	
        self.digital_pfb_clock_sync_xxx_0_0 = digital.pfb_clock_sync_ccf(sps, 3.14*2/100, (rrc_taps), 32, 0, 1.5, 1)
        self.digital_packet_headerparser_b_0 = digital.packet_headerparser_b(header_formatter.base())
        self.digital_packet_headergenerator_bb_0_0 = digital.packet_headergenerator_bb(header_formatter, "packet_len")
        self.digital_header_payload_demux_0 = digital.header_payload_demux(
        	  16,
        	  1,
        	  0,
        	  "packet_len",
        	  "packet_len",
        	  True,
        	  gr.sizeof_gr_complex,
        	  "",
                  samp_rate,
                  (),
            )
        self.digital_correlate_and_sync_cc_0 = digital.correlate_and_sync_cc((preamble), (matched_filter), sps)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(constel_payload.base())
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(constel_header.base())
        self.digital_chunks_to_symbols_xx_0_1 = digital.chunks_to_symbols_bc((constel_header.points()), 1)
        self.digital_chunks_to_symbols_xx_0_0_0 = digital.chunks_to_symbols_bc((constel_payload.points()), 1)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=0.0,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_vector_source_x_0_0 = blocks.vector_source_c(preamble, True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate/2,True)
        self.blocks_tagged_stream_mux_0_0 = blocks.tagged_stream_mux(gr.sizeof_gr_complex*1, "packet_len", 0)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_gr_complex * 1, False)
        self.blocks_stream_to_tagged_stream_0_1 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 50, "packet_len")
        self.blocks_stream_to_tagged_stream_0_0_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_gr_complex, 1, 100, "packet_len")
        self.blocks_stream_to_tagged_stream_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_gr_complex, 1, 64, "packet_len")
        self.blocks_repack_bits_bb_0_2 = blocks.repack_bits_bb(constel_payload.bits_per_symbol(), 8, "", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0_1 = blocks.repack_bits_bb(8, constel_payload.bits_per_symbol(), "", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(constel_payload.bits_per_symbol(), constel_payload.bits_per_symbol(), "packet_len", False, gr.GR_LSB_FIRST)
        self.blocks_null_source_0_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_imag_0 = blocks.complex_to_imag(1)
        self.blocks_char_to_float_1 = blocks.char_to_float(1, 1)
        self.analog_random_source_x_0_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 10)), True)
        self.analog_agc2_xx_0_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0_0.set_max_gain(5)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.digital_packet_headerparser_b_0, 'header_data'), (self.digital_header_payload_demux_0, 'header_data'))    
        self.connect((self.analog_agc2_xx_0_0, 0), (self.digital_correlate_and_sync_cc_0, 0))    
        self.connect((self.analog_agc2_xx_0_0, 0), (self.qtgui_time_sink_x_0_1_0_0_0, 0))    
        self.connect((self.analog_random_source_x_0_0, 0), (self.blocks_repack_bits_bb_0_1, 0))    
        self.connect((self.blocks_char_to_float_1, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.blocks_char_to_float_1, 0), (self.qtgui_time_sink_x_1, 1))    
        self.connect((self.blocks_complex_to_imag_0, 0), (self.qtgui_time_sink_x_0_2, 1))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.qtgui_time_sink_x_0_2, 0))    
        self.connect((self.blocks_null_source_0, 0), (self.qtgui_time_sink_x_1, 0))    
        self.connect((self.blocks_null_source_0_0, 0), (self.blocks_stream_to_tagged_stream_0_0_0_0, 0))    
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0_0, 0))    
        self.connect((self.blocks_repack_bits_bb_0_1, 0), (self.blocks_stream_to_tagged_stream_0_1, 0))    
        self.connect((self.blocks_repack_bits_bb_0_2, 0), (self.digital_packet_headergenerator_bb_0_0, 0))    
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.blocks_tagged_stream_mux_0_0, 0))    
        self.connect((self.blocks_stream_to_tagged_stream_0_0_0_0, 0), (self.blocks_tagged_stream_mux_0_0, 3))    
        self.connect((self.blocks_stream_to_tagged_stream_0_1, 0), (self.blocks_repack_bits_bb_0_0, 0))    
        self.connect((self.blocks_stream_to_tagged_stream_0_1, 0), (self.blocks_repack_bits_bb_0_2, 0))    
        self.connect((self.blocks_tag_gate_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_tagged_stream_mux_0_0, 0), (self.pfb_arb_resampler_xxx_0, 0))    
        self.connect((self.blocks_tagged_stream_mux_0_0, 0), (self.qtgui_time_sink_x_0_3, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_stream_to_tagged_stream_0_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.analog_agc2_xx_0_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0_0_0, 0), (self.blocks_tagged_stream_mux_0_0, 2))    
        self.connect((self.digital_chunks_to_symbols_xx_0_1, 0), (self.blocks_tagged_stream_mux_0_0, 1))    
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_packet_headerparser_b_0, 0))    
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.blocks_char_to_float_1, 0))    
        self.connect((self.digital_correlate_and_sync_cc_0, 1), (self.blocks_complex_to_imag_0, 0))    
        self.connect((self.digital_correlate_and_sync_cc_0, 1), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.digital_correlate_and_sync_cc_0, 0), (self.digital_pfb_clock_sync_xxx_0_0, 0))    
        self.connect((self.digital_correlate_and_sync_cc_0, 0), (self.qtgui_time_sink_x_0_1_0_0_0_0, 0))    
        self.connect((self.digital_header_payload_demux_0, 0), (self.digital_constellation_decoder_cb_0, 0))    
        self.connect((self.digital_header_payload_demux_0, 1), (self.digital_constellation_decoder_cb_0_0, 0))    
        self.connect((self.digital_header_payload_demux_0, 0), (self.qtgui_const_sink_x_0_0, 0))    
        self.connect((self.digital_header_payload_demux_0, 0), (self.qtgui_time_sink_x_0_1_0_0_1, 0))    
        self.connect((self.digital_header_payload_demux_0, 1), (self.qtgui_time_sink_x_0_1_0_0_1_0, 0))    
        self.connect((self.digital_packet_headergenerator_bb_0_0, 0), (self.digital_chunks_to_symbols_xx_0_1, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0_0, 0), (self.digital_header_payload_demux_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0_0, 0), (self.qtgui_time_sink_x_0_1_0_0_2, 0))    
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_tag_gate_0, 0))    
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.qtgui_time_sink_x_0_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "basic_chain")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_matched_filter(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, 11*self.sps*self.nfilts))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.eb, 5*self.sps*self.nfilts))
        self.set_rrc_taps_enc(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, 11*self.sps*self.nfilts))
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_matched_filter(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, 11*self.sps*self.nfilts))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.eb, 5*self.sps*self.nfilts))
        self.set_rrc_taps_enc(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, 11*self.sps*self.nfilts))

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.set_matched_filter(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, 11*self.sps*self.nfilts))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.eb, 5*self.sps*self.nfilts))
        self.set_rrc_taps_enc(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, 11*self.sps*self.nfilts))

    def get_constel_header(self):
        return self.constel_header

    def set_constel_header(self, constel_header):
        self.constel_header = constel_header
        self.set_header_formatter(digital.packet_header_default(4, "packet_len", "packet_num", self.constel_header.bits_per_symbol()))
        self.digital_chunks_to_symbols_xx_0_1.set_symbol_table((self.constel_header.points()))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate/2)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1_0_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1_0_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1_0_0_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1_0_0_2.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_2.set_samp_rate(self.samp_rate*2)
        self.qtgui_time_sink_x_0_3.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)

    def get_rrc_taps_enc(self):
        return self.rrc_taps_enc

    def set_rrc_taps_enc(self, rrc_taps_enc):
        self.rrc_taps_enc = rrc_taps_enc
        self.pfb_arb_resampler_xxx_0.set_taps((self.rrc_taps_enc))

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0_0.update_taps((self.rrc_taps))

    def get_preamble(self):
        return self.preamble

    def set_preamble(self, preamble):
        self.preamble = preamble
        self.blocks_vector_source_x_0_0.set_data(self.preamble, [])

    def get_matched_filter(self):
        return self.matched_filter

    def set_matched_filter(self, matched_filter):
        self.matched_filter = matched_filter

    def get_header_formatter(self):
        return self.header_formatter

    def set_header_formatter(self, header_formatter):
        self.header_formatter = header_formatter
        self.digital_packet_headergenerator_bb_0_0.set_header_formatter(self.header_formatter)

    def get_constel_preamble(self):
        return self.constel_preamble

    def set_constel_preamble(self, constel_preamble):
        self.constel_preamble = constel_preamble

    def get_constel_payload(self):
        return self.constel_payload

    def set_constel_payload(self, constel_payload):
        self.constel_payload = constel_payload
        self.blocks_repack_bits_bb_0_0.set_k_and_l(self.constel_payload.bits_per_symbol(),self.constel_payload.bits_per_symbol())
        self.blocks_repack_bits_bb_0_1.set_k_and_l(8,self.constel_payload.bits_per_symbol())
        self.blocks_repack_bits_bb_0_2.set_k_and_l(self.constel_payload.bits_per_symbol(),8)
        self.digital_chunks_to_symbols_xx_0_0_0.set_symbol_table((self.constel_payload.points()))


def main(top_block_cls=basic_chain, options=None):

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
