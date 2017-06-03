#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Test Time Phase Sync
# Generated: Sun May 28 22:20:56 2017
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
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
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
from gnuradio import qtgui


class test_time_phase_sync(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Test Time Phase Sync")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Test Time Phase Sync")
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

        self.settings = Qt.QSettings("GNU Radio", "test_time_phase_sync")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.time_offset = time_offset = 1
        self.sps = sps = 4
        self.samp_rate = samp_rate = 32000
        self.phase_offset = phase_offset = 0
        self.noise = noise = 0.01
        self.nfilts = nfilts = 32
        self.freq_offset = freq_offset = 0
        self.eb = eb = 0.35
        self.time_offset_label = time_offset_label = time_offset
        self.spacer_label2 = spacer_label2 = "-----------------------------------"
        self.spacer_label1 = spacer_label1 = "----------------------------------"
        self.samp_rate_label = samp_rate_label = samp_rate
        self.rrc_taps_clocksync = rrc_taps_clocksync = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), eb, 11*sps*nfilts)
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 11*sps*nfilts)
        self.phase_offset_label = phase_offset_label = phase_offset
        self.noise_label = noise_label = noise
        self.freq_offset_label = freq_offset_label = freq_offset
        self.delay = delay = 29
        self.constel = constel = digital.constellation_bpsk()

        ##################################################
        # Blocks
        ##################################################
        self._time_offset_range = Range(0.99, 1.01, 0.00001, 1, 200)
        self._time_offset_win = RangeWidget(self._time_offset_range, self.set_time_offset, 'Timing Offset', "slider", float)
        self.top_grid_layout.addWidget(self._time_offset_win, 20,2,1,1)
        self._samp_rate_range = Range(1, 256000, 10, 32000, 100)
        self._samp_rate_win = RangeWidget(self._samp_rate_range, self.set_samp_rate, 'Sample rate', "slider", int)
        self.top_grid_layout.addWidget(self._samp_rate_win, 0,0,1,1)
        self._phase_offset_range = Range(-2*3.14, 2*3.14, 0.01, 0, 200)
        self._phase_offset_win = RangeWidget(self._phase_offset_range, self.set_phase_offset, 'Phase Offset', "slider", float)
        self.top_grid_layout.addWidget(self._phase_offset_win, 21,2,1,1)
        self._noise_range = Range(0, 1, 0.005, 0.01, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, 'Noise', "slider", float)
        self.top_grid_layout.addWidget(self._noise_win, 20,0,1,1)
        self._freq_offset_range = Range(-0.05, 0.05, 0.0001, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, 'Frequency Offset', "slider", float)
        self.top_grid_layout.addWidget(self._freq_offset_win, 21,0,1,1)
        self._delay_range = Range(0, 100, 1, 29, 100)
        self._delay_win = RangeWidget(self._delay_range, self.set_delay, 'Delay', "slider", int)
        self.top_grid_layout.addWidget(self._delay_win, 23,0,1,1)
        self._time_offset_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._time_offset_label_formatter = None
        else:
          self._time_offset_label_formatter = lambda x: x

        self._time_offset_label_tool_bar.addWidget(Qt.QLabel('Timing offset'+": "))
        self._time_offset_label_label = Qt.QLabel(str(self._time_offset_label_formatter(self.time_offset_label)))
        self._time_offset_label_tool_bar.addWidget(self._time_offset_label_label)
        self.top_grid_layout.addWidget(self._time_offset_label_tool_bar, 20,3,1,1)

        self._spacer_label2_tool_bar = Qt.QToolBar(self)

        if None:
          self._spacer_label2_formatter = None
        else:
          self._spacer_label2_formatter = lambda x: x

        self._spacer_label2_tool_bar.addWidget(Qt.QLabel('  '+": "))
        self._spacer_label2_label = Qt.QLabel(str(self._spacer_label2_formatter(self.spacer_label2)))
        self._spacer_label2_tool_bar.addWidget(self._spacer_label2_label)
        self.top_grid_layout.addWidget(self._spacer_label2_tool_bar, 100,3,1,1)

        self._spacer_label1_tool_bar = Qt.QToolBar(self)

        if None:
          self._spacer_label1_formatter = None
        else:
          self._spacer_label1_formatter = lambda x: x

        self._spacer_label1_tool_bar.addWidget(Qt.QLabel('  '+": "))
        self._spacer_label1_label = Qt.QLabel(str(self._spacer_label1_formatter(self.spacer_label1)))
        self._spacer_label1_tool_bar.addWidget(self._spacer_label1_label)
        self.top_grid_layout.addWidget(self._spacer_label1_tool_bar, 100,1,1,1)

        self._samp_rate_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._samp_rate_label_formatter = None
        else:
          self._samp_rate_label_formatter = lambda x: x

        self._samp_rate_label_tool_bar.addWidget(Qt.QLabel('Sample rate'+": "))
        self._samp_rate_label_label = Qt.QLabel(str(self._samp_rate_label_formatter(self.samp_rate_label)))
        self._samp_rate_label_tool_bar.addWidget(self._samp_rate_label_label)
        self.top_grid_layout.addWidget(self._samp_rate_label_tool_bar, 0,1,1,1)

        self.qtgui_time_sink_x_0_0_3 = qtgui.time_sink_c(
        	64, #size
        	samp_rate, #samp_rate
        	"Mapped symbols", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_3.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_3.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0_3.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_3.enable_tags(-1, False)
        self.qtgui_time_sink_x_0_0_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_3.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_3.enable_grid(False)
        self.qtgui_time_sink_x_0_0_3.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_3.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_0_3.disable_legend()

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
                    self.qtgui_time_sink_x_0_0_3.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_3.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_3.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_3.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_3.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_3.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_3.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_3.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_3_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_3.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_3_win, 2,0,1,2)
        self.qtgui_time_sink_x_0_0_1_0_0_0 = qtgui.time_sink_c(
        	256, #size
        	samp_rate, #samp_rate
        	'Time and phase synced symbols', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1_0_0_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0_1_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1_0_0_0.enable_tags(-1, False)
        self.qtgui_time_sink_x_0_0_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_1_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_0_1_0_0_0.disable_legend()

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
                    self.qtgui_time_sink_x_0_0_1_0_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_1_0_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_1_0_0_0_win, 4,2,1,2)
        self.qtgui_time_sink_x_0_0_1_0_0 = qtgui.time_sink_c(
        	256, #size
        	samp_rate, #samp_rate
        	'Time synced symbols', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1_0_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0_1_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1_0_0.enable_tags(-1, False)
        self.qtgui_time_sink_x_0_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_1_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_0_1_0_0.disable_legend()

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
                    self.qtgui_time_sink_x_0_0_1_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_1_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_1_0_0_win, 4,0,1,2)
        self.qtgui_time_sink_x_0_0_1_0 = qtgui.time_sink_c(
        	512*2, #size
        	samp_rate, #samp_rate
        	'RX symbols', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1_0.enable_tags(-1, False)
        self.qtgui_time_sink_x_0_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_0_1_0.disable_legend()

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
                    self.qtgui_time_sink_x_0_0_1_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_1_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_1_0_win, 3,2,1,2)
        self.qtgui_time_sink_x_0_0_1 = qtgui.time_sink_c(
        	512*2, #size
        	samp_rate, #samp_rate
        	'TX symbols', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1.enable_tags(-1, False)
        self.qtgui_time_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_0_1.disable_legend()

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
                    self.qtgui_time_sink_x_0_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_1_win, 3,0,1,2)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	'Data output', #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, False)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()

        labels = ["Source data", "Received data", "Difference", "Data out", '',
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

        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win, 8,0,1,4)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
        	64*4, #size
        	samp_rate, #samp_rate
        	"Pulse shaped symbols", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1.5, 1.5)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, False)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 2,2,1,2)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0.5,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("BER")

        labels = ['BER', '', '', '', '',
                  '', '', '', '', '']
        units = ['1', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -10)
            self.qtgui_number_sink_0.set_max(i, 0)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(True)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 6,2,1,2)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Channel spectrum", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ["At transmitter", "At receiver", "At receiver after tracking", '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 6,0,1,2)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	512, #size
        	"Constellations before Costas Loop", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_win, 5,0,1,2)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	512, #size
        	"Constellations after Costas Loop", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
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
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 5,2,1,2)
        self._phase_offset_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._phase_offset_label_formatter = None
        else:
          self._phase_offset_label_formatter = lambda x: x

        self._phase_offset_label_tool_bar.addWidget(Qt.QLabel('Phase offset'+": "))
        self._phase_offset_label_label = Qt.QLabel(str(self._phase_offset_label_formatter(self.phase_offset_label)))
        self._phase_offset_label_tool_bar.addWidget(self._phase_offset_label_label)
        self.top_grid_layout.addWidget(self._phase_offset_label_tool_bar, 21,3,1,1)

        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(rrc_taps),
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)

        self._noise_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._noise_label_formatter = None
        else:
          self._noise_label_formatter = lambda x: x

        self._noise_label_tool_bar.addWidget(Qt.QLabel('Noise'+": "))
        self._noise_label_label = Qt.QLabel(str(self._noise_label_formatter(self.noise_label)))
        self._noise_label_tool_bar.addWidget(self._noise_label_label)
        self.top_grid_layout.addWidget(self._noise_label_tool_bar, 20,1,1,1)

        self._freq_offset_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._freq_offset_label_formatter = None
        else:
          self._freq_offset_label_formatter = lambda x: x

        self._freq_offset_label_tool_bar.addWidget(Qt.QLabel('Freq offset label'+": "))
        self._freq_offset_label_label = Qt.QLabel(str(self._freq_offset_label_formatter(self.freq_offset_label)))
        self._freq_offset_label_tool_bar.addWidget(self._freq_offset_label_label)
        self.top_grid_layout.addWidget(self._freq_offset_label_tool_bar, 21,1,1,1)

        self.fec_ber_bf_0 = fec.ber_bf(False, 100, -7.0)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 2*3.14/100, (rrc_taps_clocksync), 32, 0, 0.5, 1)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(3.14*2/100, 2**constel.bits_per_symbol(), False)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(constel.base())
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((constel.points()), 1)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise,
        	frequency_offset=freq_offset,
        	epsilon=time_offset,
        	taps=(1.0+phase_offset*1j, ),
        	noise_seed=0,
        	block_tags=True
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_char*1, (20,0))
        self.blocks_repack_bits_bb_1 = blocks.repack_bits_bb(8, constel.bits_per_symbol(), "", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(constel.bits_per_symbol(), 8, "", False, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(constel.bits_per_symbol(), 8, "", False, gr.GR_LSB_FIRST)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_gr_complex*1, 20)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_char*1, delay)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self.analog_random_source_x_0_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 10000)), True)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 0+1, 1000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.analog_random_source_x_0_0, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.blocks_abs_xx_0, 0), (self.qtgui_time_sink_x_0_0_0, 2))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0_0_0, 1))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.blocks_delay_1, 0), (self.qtgui_time_sink_x_0_0_3, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.fec_ber_bf_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.fec_ber_bf_0, 1))
        self.connect((self.blocks_repack_bits_bb_1, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_repack_bits_bb_1, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.blocks_repack_bits_bb_1, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_abs_xx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_time_sink_x_0_0_1_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_delay_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_time_sink_x_0_0_1_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_time_sink_x_0_0_1_0_0, 0))
        self.connect((self.fec_ber_bf_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.qtgui_time_sink_x_0_0_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "test_time_phase_sync")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset
        self.set_time_offset_label(self._time_offset_label_formatter(self.time_offset))
        self.channels_channel_model_0.set_timing_offset(self.time_offset)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps_clocksync(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.eb, 11*self.sps*self.nfilts))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, 11*self.sps*self.nfilts))
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_rate_label(self._samp_rate_label_formatter(self.samp_rate))
        self.qtgui_time_sink_x_0_0_3.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_1_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_1_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_phase_offset(self):
        return self.phase_offset

    def set_phase_offset(self, phase_offset):
        self.phase_offset = phase_offset
        self.set_phase_offset_label(self._phase_offset_label_formatter(self.phase_offset))
        self.channels_channel_model_0.set_taps((1.0+self.phase_offset*1j, ))

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.set_noise_label(self._noise_label_formatter(self.noise))
        self.channels_channel_model_0.set_noise_voltage(self.noise)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps_clocksync(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.eb, 11*self.sps*self.nfilts))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, 11*self.sps*self.nfilts))

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.set_freq_offset_label(self._freq_offset_label_formatter(self.freq_offset))
        self.channels_channel_model_0.set_frequency_offset(self.freq_offset)

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.set_rrc_taps_clocksync(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.eb, 11*self.sps*self.nfilts))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.eb, 11*self.sps*self.nfilts))

    def get_time_offset_label(self):
        return self.time_offset_label

    def set_time_offset_label(self, time_offset_label):
        self.time_offset_label = time_offset_label
        Qt.QMetaObject.invokeMethod(self._time_offset_label_label, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.time_offset_label)))

    def get_spacer_label2(self):
        return self.spacer_label2

    def set_spacer_label2(self, spacer_label2):
        self.spacer_label2 = spacer_label2
        Qt.QMetaObject.invokeMethod(self._spacer_label2_label, "setText", Qt.Q_ARG("QString", str(self.spacer_label2)))

    def get_spacer_label1(self):
        return self.spacer_label1

    def set_spacer_label1(self, spacer_label1):
        self.spacer_label1 = spacer_label1
        Qt.QMetaObject.invokeMethod(self._spacer_label1_label, "setText", Qt.Q_ARG("QString", str(self.spacer_label1)))

    def get_samp_rate_label(self):
        return self.samp_rate_label

    def set_samp_rate_label(self, samp_rate_label):
        self.samp_rate_label = samp_rate_label
        Qt.QMetaObject.invokeMethod(self._samp_rate_label_label, "setText", Qt.Q_ARG("QString", str(self.samp_rate_label)))

    def get_rrc_taps_clocksync(self):
        return self.rrc_taps_clocksync

    def set_rrc_taps_clocksync(self, rrc_taps_clocksync):
        self.rrc_taps_clocksync = rrc_taps_clocksync
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps_clocksync))

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.pfb_arb_resampler_xxx_0.set_taps((self.rrc_taps))

    def get_phase_offset_label(self):
        return self.phase_offset_label

    def set_phase_offset_label(self, phase_offset_label):
        self.phase_offset_label = phase_offset_label
        Qt.QMetaObject.invokeMethod(self._phase_offset_label_label, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.phase_offset_label)))

    def get_noise_label(self):
        return self.noise_label

    def set_noise_label(self, noise_label):
        self.noise_label = noise_label
        Qt.QMetaObject.invokeMethod(self._noise_label_label, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.noise_label)))

    def get_freq_offset_label(self):
        return self.freq_offset_label

    def set_freq_offset_label(self, freq_offset_label):
        self.freq_offset_label = freq_offset_label
        Qt.QMetaObject.invokeMethod(self._freq_offset_label_label, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.freq_offset_label)))

    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        self.delay = delay
        self.blocks_delay_0.set_dly(self.delay)

    def get_constel(self):
        return self.constel

    def set_constel(self, constel):
        self.constel = constel


def main(top_block_cls=test_time_phase_sync, options=None):

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
