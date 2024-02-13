#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.8.0

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
import numpy
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
import numpy as np
import sip



class ASKProbando(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
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

        self.settings = Qt.QSettings("GNU Radio", "ASKProbando")

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

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "DEMODULACION ASK", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.5)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Senal Digital Bandabase', 'Senal Modulada', 'Signal 3', 'Signal 4', 'Signal 5',
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


        for i in range(2):
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
        self.plot_rectangular = qtgui.time_sink_f(
            (32*sps), #size
            samp_rate, #samp_rate
            "MODULACION ASK", #name
            2, #number of inputs
            None # parent
        )
        self.plot_rectangular.set_update_time(0.10)
        self.plot_rectangular.set_y_axis(-1, 1)

        self.plot_rectangular.set_y_label('Amplitude', "")

        self.plot_rectangular.enable_tags(True)
        self.plot_rectangular.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.plot_rectangular.enable_autoscale(True)
        self.plot_rectangular.enable_grid(False)
        self.plot_rectangular.enable_axis_labels(True)
        self.plot_rectangular.enable_control_panel(True)
        self.plot_rectangular.enable_stem_plot(False)


        labels = ['Señal Cuadratica', 'Modulacion ASK', 'Signal 3', 'Signal 4', 'Signal 5',
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


        for i in range(2):
            if len(labels[i]) == 0:
                self.plot_rectangular.set_line_label(i, "Data {0}".format(i))
            else:
                self.plot_rectangular.set_line_label(i, labels[i])
            self.plot_rectangular.set_line_width(i, widths[i])
            self.plot_rectangular.set_line_color(i, colors[i])
            self.plot_rectangular.set_line_style(i, styles[i])
            self.plot_rectangular.set_line_marker(i, markers[i])
            self.plot_rectangular.set_line_alpha(i, alphas[i])

        self._plot_rectangular_win = sip.wrapinstance(self.plot_rectangular.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._plot_rectangular_win)
        self.multiply = blocks.multiply_vff(1)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_fff(sps, h)
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.blocks_throttle2_1_0 = blocks.throttle( gr.sizeof_gr_complex*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_throttle2_1 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_threshold_ff_0 = blocks.threshold_ff((500e-6), (500e-6), 0)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 0)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 10e3, 1, 0, 0)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 2, int(1e6)))), True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.multiply, 1))
        self.connect((self.blocks_char_to_float_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_throttle2_1, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_throttle2_1_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle2_1, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_throttle2_1_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.blocks_throttle2_1_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.multiply, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.plot_rectangular, 0))
        self.connect((self.multiply, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.multiply, 0), (self.plot_rectangular, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ASKProbando")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h
        self.set_sps(len(self.h))
        self.interp_fir_filter_xxx_0.set_taps(self.h)

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

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_1_0.set_sample_rate(self.samp_rate)
        self.plot_rectangular.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)




def main(top_block_cls=ASKProbando, options=None):

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
