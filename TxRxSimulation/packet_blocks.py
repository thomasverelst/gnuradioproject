#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Packet Blocks
# Generated: Sat Mar 11 16:16:44 2017
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
import packetizr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import scipy
import sip
import sys


class packet_blocks(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Packet Blocks")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Packet Blocks")
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

        self.settings = Qt.QSettings("GNU Radio", "packet_blocks")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.eb = eb = 0.35
        self.variable_constellation_0PSK = variable_constellation_0PSK = digital.constellation_calcdist(([-1-1j, -1+1j, 1+1j, 1-1j]), ([0, 1, 3, 2]), 4, 1).base()
        self.variable_constellation_0 = variable_constellation_0 = digital.constellation_calcdist(([-1-1j, -1+1j, 1+1j, 1-1j]), ([0, 1, 3, 2]), 4, 1).base()
        self.time_offset = time_offset = 1
        self.samp_rate = samp_rate = 32000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), eb, 5*sps*nfilts)
        self.preamble = preamble = [1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,-1,-1,1,-1,1,1,1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,-1,-1]
        self.phase = phase = 0
        self.payload_size = payload_size = 64
        self.noise = noise = 0
        self.matched_filter = matched_filter = firdes.root_raised_cosine(nfilts, nfilts, 1, eb, int(11*sps*nfilts))
        self.gap = gap = 20000
        self.freq_offset = freq_offset = 0
        self.constel_bpsk = constel_bpsk = digital.constellation_calcdist(([1,- 1]), ([0,1]), 2, 1).base()
        self.bb_filter = bb_filter = firdes.root_raised_cosine(sps, sps, 1, eb, 101)

        ##################################################
        # Blocks
        ##################################################
        self._time_offset_range = Range(0.995, 1.005, 0.00001, 1, 200)
        self._time_offset_win = RangeWidget(self._time_offset_range, self.set_time_offset, "Timing Offset", "slider", float)
        self.top_grid_layout.addWidget(self._time_offset_win, 4,1,1,1)
        self.qtgui_time_sink_x_1_0_0_1_0 = qtgui.time_sink_f(
        	800, #size
        	samp_rate, #samp_rate
        	"Encoded", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_0_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0_0_1_0.set_y_axis(-5, 5)
        
        self.qtgui_time_sink_x_1_0_0_1_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_1_0_0_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0_1_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1_0_0_1_0.disable_legend()
        
        labels = ["|corr|^2", "Re{corr}", "Im{corr}", "", "",
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
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_0_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_0_1_0_win)
        self._phase_range = Range(-2*scipy.pi, 2*scipy.pi, 0.1, 0, 200)
        self._phase_win = RangeWidget(self._phase_range, self.set_phase, "Phase offset", "slider", float)
        self.top_grid_layout.addWidget(self._phase_win, 3,1,1,1)
        self._noise_range = Range(0, 1, 0.005, 0, 200)
        self._noise_win = RangeWidget(self._noise_range, self.set_noise, "Noise", "slider", float)
        self.top_grid_layout.addWidget(self._noise_win, 3,0,1,1)
        self._freq_offset_range = Range(-0.001, 0.001, 0.00002, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, "Frequency Offset", "slider", float)
        self.top_grid_layout.addWidget(self._freq_offset_win, 4,0,1,1)
        print "DEBUG", type(constel_bpsk)
        self.digital_constellation_decoder_cb_1 = digital.constellation_decoder_cb(constel_bpsk)
        self.penc = packetizr.packet_encoder (1, 0, constel_bpsk, constel_bpsk, 1, "packet_len") #itemsize is in bytes

        self.blocks_vector_source_x_0 = blocks.vector_source_c((1,2,3), True, 1, [])
        self.blocks_vector_sink_x_0 = blocks.vector_sink_c(1)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate/10,True)
        self.blocks_char_to_float_1_0 = blocks.char_to_float(1, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_1_0, 0), (self.blocks_throttle_0_0, 0))    
        self.connect((self.blocks_throttle_0_0, 0), (self.qtgui_time_sink_x_1_0_0_1_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_vector_sink_x_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.digital_constellation_decoder_cb_1, 0))    
        self.connect((self.digital_constellation_decoder_cb_1, 0), (self.blocks_char_to_float_1_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "packet_blocks")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_bb_filter(firdes.root_raised_cosine(self.sps, self.sps, 1, self.eb, 101))
        self.set_matched_filter(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1, self.eb, int(11*self.sps*self.nfilts)))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.eb, 5*self.sps*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_matched_filter(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1, self.eb, int(11*self.sps*self.nfilts)))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.eb, 5*self.sps*self.nfilts))

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.set_bb_filter(firdes.root_raised_cosine(self.sps, self.sps, 1, self.eb, 101))
        self.set_matched_filter(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1, self.eb, int(11*self.sps*self.nfilts)))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.eb, 5*self.sps*self.nfilts))

    def get_variable_constellation_0PSK(self):
        return self.variable_constellation_0PSK

    def set_variable_constellation_0PSK(self, variable_constellation_0PSK):
        self.variable_constellation_0PSK = variable_constellation_0PSK

    def get_variable_constellation_0(self):
        return self.variable_constellation_0

    def set_variable_constellation_0(self, variable_constellation_0):
        self.variable_constellation_0 = variable_constellation_0

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate/10)
        self.qtgui_time_sink_x_1_0_0_1_0.set_samp_rate(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps

    def get_preamble(self):
        return self.preamble

    def set_preamble(self, preamble):
        self.preamble = preamble

    def get_phase(self):
        return self.phase

    def set_phase(self, phase):
        self.phase = phase

    def get_payload_size(self):
        return self.payload_size

    def set_payload_size(self, payload_size):
        self.payload_size = payload_size

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise

    def get_matched_filter(self):
        return self.matched_filter

    def set_matched_filter(self, matched_filter):
        self.matched_filter = matched_filter

    def get_gap(self):
        return self.gap

    def set_gap(self, gap):
        self.gap = gap

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset

    def get_constel_bpsk(self):
        return self.constel_bpsk

    def set_constel_bpsk(self, constel_bpsk):
        self.constel_bpsk = constel_bpsk

    def get_bb_filter(self):
        return self.bb_filter

    def set_bb_filter(self, bb_filter):
        self.bb_filter = bb_filter


def main(top_block_cls=packet_blocks, options=None):

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
