#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Q2_ASymmetricFilter
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

class Q2_ASymmetricFilter(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Q2_ASymmetricFilter")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Q2_ASymmetricFilter")
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

        self.settings = Qt.QSettings("GNU Radio", "Q2_ASymmetricFilter")

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
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "After Filtering", #name
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
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Before Filter", #name
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
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(1, [1.82810418e-18+0.00000000e+00j, -6.27557028e-05+1.93142193e-04j,
               -2.73533732e-04-1.98733889e-04j,  2.84176491e-04-2.06466306e-04j,
                7.03194623e-05+2.16421052e-04j,  7.01364264e-19-2.57677050e-34j,
               -7.90625600e-05+2.43329539e-04j, -3.58481976e-04-2.60452401e-04j,
                3.85574235e-04-2.80136080e-04j,  9.82780851e-05+3.02468845e-04j,
               -1.14880270e-18+8.44126530e-34j, -1.15490686e-04+3.55443782e-04j,
               -5.31658044e-04-3.86272179e-04j,  5.78249128e-04-4.20122584e-04j,
                1.48518963e-04+4.57094368e-04j,  1.30730452e-18+3.20359099e-33j,
               -1.75721482e-04+5.40815112e-04j, -8.09009023e-04-5.87779460e-04j,
                8.78540184e-04-6.38296806e-04j,  2.25002242e-04+6.92485696e-04j,
                6.57792451e-18-9.66676104e-33j, -2.63958049e-04+8.12379343e-04j,
               -1.20894534e-03-8.78350203e-04j,  1.30553445e-03-9.48526302e-04j,
                3.32412245e-04+1.02305970e-03j,  2.41441247e-18+4.14251245e-33j,
               -3.85307376e-04+1.18585417e-03j, -1.75415811e-03-1.27447047e-03j,
                1.88310687e-03-1.36815723e-03j,  4.76698067e-04+1.46712579e-03j,
                3.09864281e-18+1.51866440e-32j, -5.46462614e-04+1.68183899e-03j,
               -2.47486982e-03-1.79809818e-03j,  2.64358021e-03-1.92067345e-03j,
                6.66047564e-04+2.04988362e-03j,  3.83125907e-18+5.82037604e-32j,
               -7.56946437e-04+2.32964159e-03j, -3.41480077e-03-2.48099799e-03j,
                3.63449751e-03-2.64061701e-03j,  9.12706022e-04+2.80902030e-03j,
                4.58024243e-18-1.34620301e-32j, -1.03148170e-03+3.17457424e-03j,
               -4.64268085e-03-3.37310508e-03j,  4.93185734e-03-3.58320410e-03j,
                1.23657977e-03+3.80580120e-03j,  5.31285869e-18+3.90579837e-32j,
               -1.39483506e-03+4.29286090e-03j, -6.27617193e-03-4.55990582e-03j,
                6.66812028e-03-4.84467297e-03j,  1.67301025e-03+5.14899610e-03j,
                5.99708903e-18+2.05789328e-32j, -1.89272097e-03+5.82519618e-03j,
               -8.53700198e-03-6.20249500e-03j,  9.09839701e-03-6.61037236e-03j,
                2.29164729e-03+7.05296515e-03j,  6.60302929e-18-3.22637718e-33j,
               -2.61990538e-03+8.06323967e-03j, -1.18978915e-02-8.64432415e-03j,
                1.27833126e-02-9.28762024e-03j,  3.25067253e-03+1.00045413e-02j,
                7.10419698e-18+6.96362356e-32j, -3.80847651e-03+1.17212854e-02j,
               -1.75682609e-02-1.27640887e-02j,  1.92286984e-02-1.39704671e-02j,
                4.99881127e-03+1.53847592e-02j,  7.47868865e-18+4.39897852e-32j,
               -6.21021936e-03+1.91130899e-02j, -2.98006704e-02-2.16514544e-02j,
                3.42660090e-02-2.48957128e-02j,  9.48716854e-03+2.91985024e-02j,
                7.71013724e-18+2.34261882e-31j, -1.43464115e-02+4.41537145e-02j,
               -8.12593766e-02-5.90383929e-02j,  1.22135437e-01-8.87365894e-02j,
                5.77344059e-02+1.77688230e-01j, -1.99796921e-01+3.91241716e-16j,
                5.77344059e-02-1.77688230e-01j,  1.22135437e-01+8.87365894e-02j,
               -8.12593766e-02+5.90383929e-02j, -1.43464115e-02-4.41537145e-02j,
                7.71013724e-18-4.53225355e-32j,  9.48716854e-03-2.91985024e-02j,
                3.42660090e-02+2.48957128e-02j, -2.98006704e-02+2.16514544e-02j,
               -6.21021936e-03-1.91130899e-02j,  7.47868865e-18+1.39277841e-31j,
                4.99881127e-03-1.53847592e-02j,  1.92286984e-02+1.39704671e-02j,
               -1.75682609e-02+1.27640887e-02j, -3.80847651e-03-1.17212854e-02j,
                7.10419698e-18+1.04454353e-31j,  3.25067253e-03-1.00045413e-02j,
                1.27833126e-02+9.28762024e-03j, -1.18978915e-02+8.64432415e-03j,
               -2.61990538e-03-8.06323967e-03j,  6.60302929e-18+7.12010039e-32j,
                2.29164729e-03-7.05296515e-03j,  9.09839701e-03+6.61037236e-03j,
               -8.53700198e-03+6.20249500e-03j, -1.89272097e-03-5.82519618e-03j,
                5.99708903e-18+4.11578656e-32j,  1.67301025e-03-5.14899610e-03j,
                6.66812028e-03+4.84467297e-03j, -6.27617193e-03+4.55990582e-03j,
               -1.39483506e-03-4.29286090e-03j,  5.31285869e-18+1.66635558e-31j,
                1.23657977e-03-3.80580120e-03j,  4.93185734e-03+3.58320410e-03j,
               -4.64268085e-03+3.37310508e-03j, -1.03148170e-03-3.17457424e-03j,
                4.58024243e-18-4.47600306e-33j,  9.12706022e-04-2.80902030e-03j,
                3.63449751e-03+2.64061701e-03j, -3.41480077e-03+2.48099799e-03j,
               -7.56946437e-04-2.32964159e-03j,  3.83125907e-18+9.01279185e-32j,
                6.66047564e-04-2.04988362e-03j,  2.64358021e-03+1.92067345e-03j,
               -2.47486982e-03+1.79809818e-03j, -5.46462614e-04-1.68183899e-03j,
                3.09864281e-18+6.07465759e-32j,  4.76698067e-04-1.46712579e-03j,
                1.88310687e-03+1.36815723e-03j, -1.75415811e-03+1.27447047e-03j,
               -3.85307376e-04-1.18585417e-03j,  2.41441247e-18-3.07537350e-32j,
                3.32412245e-04-1.02305970e-03j,  1.30553445e-03+9.48526302e-04j,
               -1.20894534e-03+8.78350203e-04j, -2.63958049e-04-8.12379343e-04j,
                6.57792451e-18+7.73829476e-32j,  2.25002242e-04-6.92485696e-04j,
                8.78540184e-04+6.38296806e-04j, -8.09009023e-04+5.87779460e-04j,
               -1.75721482e-04-5.40815112e-04j,  1.30730452e-18+1.02544043e-32j,
                1.48518963e-04-4.57094368e-04j,  5.78249128e-04+4.20122584e-04j,
               -5.31658044e-04+3.86272179e-04j, -1.15490686e-04-3.55443782e-04j,
               -1.14880270e-18-6.98095700e-32j,  9.82780851e-05-3.02468845e-04j,
                3.85574235e-04+2.80136080e-04j, -3.58481976e-04+2.60452401e-04j,
               -7.90625600e-05-2.43329539e-04j,  7.01364264e-19+1.99365761e-32j,
                7.03194623e-05-2.16421052e-04j,  2.84176491e-04+2.06466306e-04j,
               -2.73533732e-04+1.98733889e-04j, -6.27557028e-05-1.93142193e-04j,
                1.82810418e-18-7.15957592e-33j])
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, Dynamic_generator, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 3000, 1, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Q2_ASymmetricFilter")
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





def main(top_block_cls=Q2_ASymmetricFilter, options=None):

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
