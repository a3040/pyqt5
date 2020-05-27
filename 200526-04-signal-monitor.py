# https://stackoverflow.com/questions/28258875/how-to-obtain-the-set-of-all-signals-for-a-given-widget


from PyQt5 import QtCore, QtWidgets

def get_signals(source):
    cls = source if isinstance(source, type) else type(source)
    signal = type(QtCore.pyqtSignal())
    for name in dir(source):
        if isinstance(getattr(cls, name), signal):
            print(name)

get_signals(QtWidgets.QPushButton)


print('='*50)

thread = QtCore.QThread()

metaObject = thread.staticMetaObject
for i in range(0, metaObject.methodCount()):
    method = metaObject.method(i)
    if method.methodType() == QtCore.QMetaMethod.Signal:
        print( "Signal:", method.name() ) 

print('='*50)

from typing import Iterable

from PyQt5.QtCore import pyqtBoundSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QObject



# https://stackoverflow.com/questions/2072013/how-to-intercept-all-signals-emitted-by-a-given-event-in-qt
def list_all_signals(obj: QObject) -> Iterable[pyqtBoundSignal]:
    attr_names = dir(obj)
    attributes = (getattr(obj, attr_name) for attr_name in attr_names)
    connectable = filter(lambda l: hasattr(l, "connect"), attributes)

    return connectable


class SignalListener(QObject):
    @pyqtSlot()
    def universal_slot(self, *args, **kwargs):
        print("Signal caught" + 30 * "-")
        print("sender:", self.sender())
        meta_method = (
            self.sender().metaObject().method(self.senderSignalIndex())
        )
        print("signal:", meta_method.name())
        print("signal signature:", meta_method.methodSignature())


SIGNAL_LISTENER = SignalListener()


def spy_on_all_signals(
    obj: QObject, listener: SignalListener = SIGNAL_LISTENER
):
    for signal in list_all_signals(obj):
        signal.connect(SIGNAL_LISTENER.universal_slot)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    some_line_edit = QtWidgets.QPushButton('---')
    spy_on_all_signals(some_line_edit)
    some_line_edit.show()
    app.exec_()