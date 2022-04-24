#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Q2_SymmetricFilter
# Author: gnuradio
# GNU Radio version: 3.8.2.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget

from gnuradio import qtgui

class Q2_SymmetricFilter(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Q2_SymmetricFilter")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Q2_SymmetricFilter")
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

        self.settings = Qt.QSettings("GNU Radio", "Q2_SymmetricFilter")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100000
        self.Dynamic_generator = Dynamic_generator = 1000
        self.CenterFreq = CenterFreq = 2417000000

        ##################################################
        # Blocks
        ##################################################
        self._Dynamic_generator_range = Range(100, 45000, 100, 1000, 1000)
        self._Dynamic_generator_win = RangeWidget(self._Dynamic_generator_range, self.set_Dynamic_generator, 'Choose Central Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._Dynamic_generator_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_f(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "After filter", #name
            1
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)


        self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1
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


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(1, [ 1.82810418e-18,  2.03081720e-04,  3.38106287e-04,  3.51261461e-04,
                2.27558560e-04, -7.01364264e-19, -2.55851819e-04, -4.43108091e-04,
               -4.76595965e-04, -3.18034564e-04, -1.14880270e-18,  3.73735710e-04,
                6.57165483e-04,  7.14755231e-04,  4.80617461e-04, -1.30730452e-18,
               -5.68646661e-04, -9.99990146e-04, -1.08593539e-03, -7.28122550e-04,
                6.57792451e-18,  8.54186191e-04,  1.49433862e-03,  1.61372933e-03,
                1.07570862e-03, -2.41441247e-18, -1.24688086e-03, -2.16825867e-03,
               -2.32764810e-03, -1.54262735e-03,  3.09864281e-18,  1.76839017e-03,
                3.05910734e-03,  3.26764485e-03,  2.15537519e-03, -3.83125907e-18,
               -2.44953013e-03, -4.22092589e-03, -4.49248598e-03, -2.95357873e-03,
                4.58024243e-18,  3.33794489e-03,  5.73866913e-03,  6.09611092e-03,
                4.00165619e-03, -5.31285869e-18, -4.51378107e-03, -7.75777515e-03,
               -8.24224995e-03, -5.41397489e-03,  5.99708903e-18,  6.12497373e-03,
                1.05523148e-02,  1.12462372e-02,  7.41592643e-03, -6.60302929e-18,
               -8.47819192e-03, -1.47066027e-02, -1.58010433e-02, -1.05193973e-02,
                7.10419698e-18,  1.23244889e-02,  2.17155647e-02,  2.37679783e-02,
                1.61764931e-02, -7.47868865e-18, -2.00966920e-02, -3.68356544e-02,
               -4.23551164e-02, -3.07011223e-02,  7.71013724e-18,  4.64259629e-02,
                1.00442113e-01,  1.50967703e-01,  1.86832462e-01,  1.99796921e-01,
                1.86832462e-01,  1.50967703e-01,  1.00442113e-01,  4.64259629e-02,
                7.71013724e-18, -3.07011223e-02, -4.23551164e-02, -3.68356544e-02,
               -2.00966920e-02, -7.47868865e-18,  1.61764931e-02,  2.37679783e-02,
                2.17155647e-02,  1.23244889e-02,  7.10419698e-18, -1.05193973e-02,
               -1.58010433e-02, -1.47066027e-02, -8.47819192e-03, -6.60302929e-18,
                7.41592643e-03,  1.12462372e-02,  1.05523148e-02,  6.12497373e-03,
                5.99708903e-18, -5.41397489e-03, -8.24224995e-03, -7.75777515e-03,
               -4.51378107e-03, -5.31285869e-18,  4.00165619e-03,  6.09611092e-03,
                5.73866913e-03,  3.33794489e-03,  4.58024243e-18, -2.95357873e-03,
               -4.49248598e-03, -4.22092589e-03, -2.44953013e-03, -3.83125907e-18,
                2.15537519e-03,  3.26764485e-03,  3.05910734e-03,  1.76839017e-03,
                3.09864281e-18, -1.54262735e-03, -2.32764810e-03, -2.16825867e-03,
               -1.24688086e-03, -2.41441247e-18,  1.07570862e-03,  1.61372933e-03,
                1.49433862e-03,  8.54186191e-04,  6.57792451e-18, -7.28122550e-04,
               -1.08593539e-03, -9.99990146e-04, -5.68646661e-04, -1.30730452e-18,
                4.80617461e-04,  7.14755231e-04,  6.57165483e-04,  3.73735710e-04,
               -1.14880270e-18, -3.18034564e-04, -4.76595965e-04, -4.43108091e-04,
               -2.55851819e-04, -7.01364264e-19,  2.27558560e-04,  3.51261461e-04,
                3.38106287e-04,  2.03081720e-04,  1.82810418e-18])
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, Dynamic_generator, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 3000, 1, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Q2_SymmetricFilter")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)

    def get_Dynamic_generator(self):
        return self.Dynamic_generator

    def set_Dynamic_generator(self, Dynamic_generator):
        self.Dynamic_generator = Dynamic_generator
        self.analog_sig_source_x_1.set_frequency(self.Dynamic_generator)

    def get_CenterFreq(self):
        return self.CenterFreq

    def set_CenterFreq(self, CenterFreq):
        self.CenterFreq = CenterFreq





def main(top_block_cls=Q2_SymmetricFilter, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
