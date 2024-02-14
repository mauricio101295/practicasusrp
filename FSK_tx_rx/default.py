#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: FSK_Modulation
# Author: Camila Vinza
# Copyright: @CamiVinza
# GNU Radio version: 3.10.8.0

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
import math
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import numpy as np
import sip



class default(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "FSK_Modulation", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("FSK_Modulation")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
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

        self.settings = Qt.QSettings("GNU Radio", "default")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.h = h = np.array([1,1,1,1])
        self.sps = sps = len(h)
        self.rb = rb = 32000
        self.samp_rate = samp_rate = rb*sps
        self.fsk_deviation = fsk_deviation = 100
        self.delay = delay = 145

        ##################################################
        # Blocks
        ##################################################

        self._delay_range = Range(0, 250, 1, 145, 200)
        self._delay_win = RangeWidget(self._delay_range, self.set_delay, "Retardo", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._delay_win)
        self.segunda_portadora = analog.sig_source_f(rb, analog.GR_COS_WAVE, int(1e3), 1, 0, 0)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            512, #size
            rb, #samp_rate
            "", #name
            3, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.50)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Señal de Bits Original', 'Señal Modulada', 'Señal de Bits Demodulada', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.primera_portadora = analog.sig_source_f(rb, analog.GR_COS_WAVE, int(2e3), 1, 0, 0)
        self.multiply2 = blocks.multiply_vff(1)
        self.multiply1 = blocks.multiply_vff(1)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_fcf(1,  firdes.low_pass(1,rb,1500, 400), int(1.5e3), rb)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_char*1, 100)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, int(delay))
        self.blocks_char_to_float_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 2, int(1e3)))), True)
        self.analog_quadrature_demod_cf_1 = analog.quadrature_demod_cf((rb/(2*math.pi*fsk_deviation)))
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.analog_quadrature_demod_cf_1, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.multiply1, 0))
        self.connect((self.blocks_char_to_float_1, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.multiply2, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_char_to_float_1, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_quadrature_demod_cf_1, 0))
        self.connect((self.multiply1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.multiply2, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.primera_portadora, 0), (self.multiply1, 1))
        self.connect((self.segunda_portadora, 0), (self.multiply2, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "default")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h
        self.set_sps(len(self.h))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_samp_rate(self.rb*self.sps)

    def get_rb(self):
        return self.rb

    def set_rb(self, rb):
        self.rb = rb
        self.set_samp_rate(self.rb*self.sps)
        self.analog_quadrature_demod_cf_1.set_gain((self.rb/(2*math.pi*self.fsk_deviation)))
        self.freq_xlating_fir_filter_xxx_0.set_taps( firdes.low_pass(1,self.rb,1500, 400))
        self.primera_portadora.set_sampling_freq(self.rb)
        self.qtgui_time_sink_x_0.set_samp_rate(self.rb)
        self.segunda_portadora.set_sampling_freq(self.rb)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_fsk_deviation(self):
        return self.fsk_deviation

    def set_fsk_deviation(self, fsk_deviation):
        self.fsk_deviation = fsk_deviation
        self.analog_quadrature_demod_cf_1.set_gain((self.rb/(2*math.pi*self.fsk_deviation)))

    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        self.delay = delay
        self.blocks_delay_0.set_dly(int(int(self.delay)))




def main(top_block_cls=default, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
