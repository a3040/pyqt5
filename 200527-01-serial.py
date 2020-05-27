import sys

from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure


class SerialPortManager(QtCore.QObject):
    dataChanged = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

        self._serial = QtSerialPort.QSerialPort(baudRate=115200)
        self.serial.setPortName("COM3")
        self.serial.readyRead.connect(self.on_ready_read)

    @property
    def serial(self):
        return self._serial

    def start(self):
        self.serial.open(QtCore.QIODevice.ReadOnly)

    @QtCore.pyqtSlot()
    def on_ready_read(self):
        if self.serial.canReadLine():
            line = self.serial.readLine().data().decode()
            values = line.strip().split(",")
            try:
                data = list(map(float, values))
            except ValueError as e:
                print("error", e)
            else:
                self.dataChanged.emit(data)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        fig = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(fig)

        self.max_button = QtWidgets.QPushButton(self.tr("GetMax"))
        self.all_button = QtWidgets.QPushButton(self.tr("All"))
        self.one_button = QtWidgets.QPushButton(self.tr("1"))
        self.two_button = QtWidgets.QPushButton(self.tr("2"))
        self.three_button = QtWidgets.QPushButton(self.tr("3"))
        self.four_button = QtWidgets.QPushButton(self.tr("4"))

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        hlay = QtWidgets.QHBoxLayout(central_widget)
        hlay.addWidget(self.canvas, stretch=1)

        grid_layout = QtWidgets.QGridLayout()
        grid_layout.addWidget(self.max_button, 0, 0)
        grid_layout.addWidget(self.all_button, 0, 1)
        grid_layout.addWidget(self.one_button, 1, 0)
        grid_layout.addWidget(self.two_button, 1, 1)
        grid_layout.addWidget(self.three_button, 2, 0)
        grid_layout.addWidget(self.four_button, 2, 1)

        vlay = QtWidgets.QVBoxLayout()
        vlay.addLayout(grid_layout)
        vlay.addStretch()

        hlay.addLayout(vlay)

        self.axes = self.canvas.figure.add_subplot(111)
        self.axes.set_ylim([0, 100])
        self.axes.set_title("Titre 1")
        self.axes.tick_params(
            axis="x", which="both", bottom=False, top=False, labelbottom=False
        )

        self.axes.hlines(25, -0.5, 0.5, color="g")
        self.axes.hlines(60, 1.5, 2.5, color="g")
        self.axes.hlines(50, 3.5, 4.5, color="g")
        self.axes.hlines(70, 5.5, 6.5, color="g")

        self.containers = []

        self.update_bars([0, 0, 0, 0])

        self.resize(640, 480)

    @QtCore.pyqtSlot(list)
    def update_bars(self, values):
        if len(values) == 4:
            [c.remove() for c in self.containers]
            self.containers = []
            for index, value in zip((0, 2, 4, 6), values):
                c = self.axes.bar(index, value, color="b")
                self.containers.append(c)
            self.canvas.draw()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = MainWindow()
    w.show()

    manager = SerialPortManager()
    manager.dataChanged.connect(w.update_bars)
    manager.start()

    sys.exit(app.exec_())