# https://stackoverflow.com/questions/62799886/dynamically-updating-a-qchart

import sys

#from PyQt5.QtChart import QCandlestickSeries, QChart, QChartView, QCandlestickSet
# QtChart 설치 실패 함...

from PyQt5 import QtChart
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QPointF
from PyQt5 import QtChart as qc
import time

class myCandlestick():
    def __init__(self, data):
        self.data = data
        self.app = QApplication(sys.argv)

        self.series = QtChart.QCandlestickSeries()
        self.series.setDecreasingColor(Qt.red)
        self.series.setIncreasingColor(Qt.green)

        self.ma5 = qc.QLineSeries() 
        self.tm = []

        for num, o, h, l, c, m in self.data:
            self.series.append(QtChart.QCandlestickSet(o, h, l, c))
            self.ma5.append(QPointF(num, m))
            self.tm.append(str(num))

        self.chart = QtChart.QChart()

        self.chart.addSeries(self.series)  # candle
        self.chart.addSeries(self.ma5)  # ma5 line

        self.chart.createDefaultAxes()
        self.chart.legend().hide()

        self.chart.axisX(self.series).setCategories(self.tm)
        self.chart.axisX(self.ma5).setVisible(False)

        self.chartview = QtChart.QChartView(self.chart)
        self.ui = QMainWindow()
        self.ui.setGeometry(50, 50, 500, 300)
        self.ui.setCentralWidget(self.chartview)
        self.ui.show()
        sys.exit(self.app.exec_())

    def append_data_and_plot(self, d):
        '''Append and update the plot'''
        num, o, h, l, c, m = d
        self.series.append(QtChart.QCandlestickSet(o, h, l, c))
        self.ui.show()
        #sys.exit(self.app.exec_())


data = ((1, 7380, 7520, 7380, 7510, 7324),
        (2, 7520, 7580, 7410, 7440, 7372),
        (3, 7440, 7650, 7310, 7520, 7434),
        (4, 7450, 7640, 7450, 7550, 7480),
        (5, 7510, 7590, 7460, 7490, 7502),
        (6, 7500, 7590, 7480, 7560, 7512),
        (7, 7560, 7830, 7540, 7800, 7584))

m = myCandlestick(data)

# Data is received at irregular intervals
time.sleep(1)
m.append_data_and_plot((8, 7560, 7830, 7540, 7800, 7584))

# Data is received at irregular intervals
time.sleep(0.1)
m.append_data_and_plot((9, 7450, 7640, 7450, 7550, 7480))

# Data is received at irregular intervals
time.sleep(2.5)
m.append_data_and_plot((10, 7380, 7520, 7380, 7510, 7324))