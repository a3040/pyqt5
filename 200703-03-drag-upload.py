# https://stackoverflow.com/questions/62698400/how-to-change-icons-with-the-callback-function


from functools import partial
import math
import os
import sys
import threading
import uuid

import boto3

from PyQt5.QtCore import (
    Qt,
    QUrl,
    QObject,
    pyqtSignal,
    QFileInfo,
    QDirIterator,
    QDir,
    pyqtSlot,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QListWidget,
    QPushButton,
    QProgressBar,
    QListWidgetItem,
    QStyledItemDelegate,
)

PathRole = Qt.UserRole + 1000
IdentifierRole = Qt.UserRole + 1001


class NameDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.text = QFileInfo(index.data(PathRole)).fileName()


class ListBoxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(600, 600)

        delegate = NameDelegate(self)
        self.setItemDelegate(delegate)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            icon = QIcon("loaded.png")
            for url in event.mimeData().urls():
                if url.isLocalFile():
                    fi = QFileInfo(url.toLocalFile())
                    if fi.isDir():
                        it = QDirIterator(
                            fi.fileName(), QDir.Files, QDirIterator.Subdirectories,
                        )
                        while it.hasNext():
                            item = QListWidgetItem()
                            item.setData(PathRole, it.next())
                            self.addItem(item)
                    elif fi.isFile():
                        item = QListWidgetItem()
                        item.setData(PathRole, url.toLocalFile())
                        self.addItem(item)

        else:
            event.ignore()


class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 600)

        self.listbox_view = ListBoxWidget(self)

        self.btn = QPushButton("Get Value", self)
        self.btn.setGeometry(850, 400, 200, 50)
        self.btn.clicked.connect(self.startUpload)

        self.qs3 = S3Worker("storageDomain", "awsID", "awsSecret")

        self.qs3.started.connect(self.handle_started)
        self.qs3.finished.connect(self.handle_finished)
        self.qs3.percentageChanged.connect(self.handle_percentageChanged)

        self.percentageBar_container = dict()

    def startUpload(self):
        for i in range(self.listbox_view.count()):
            item = self.listbox_view.item(i)
            filename = item.data(PathRole)
            identifier = uuid.uuid4()
            item.setData(IdentifierRole, identifier)

            # this code is for test
            displayname = str(identifier)
            bucketName = "bucketName"

            self.qs3.upload(filename, bucketName, displayname, identifier)

        if self.listbox_view.count() == 0:
            print("No File inputted")

    @pyqtSlot(uuid.UUID)
    def handle_started(self, identifier):
        if not self.percentageBar_container:
            self.btn.setEnabled(False)
        percentageBar = QProgressBar()
        percentageBar.setGeometry(500, 300, 400, 30)
        percentageBar.show()
        self.percentageBar_container[identifier] = percentageBar

    @pyqtSlot(uuid.UUID)
    def handle_finished(self, identifier):
        if self.percentageBar_container.get(identifier):
            del self.percentageBar_container[identifier]
            model = self.listbox_view.model()
            indexes = model.match(
                model.index(0, 0), IdentifierRole, identifier, -1, Qt.MatchExactly
            )
            for index in indexes:
                item = self.listbox_view.itemFromIndex(index)
                item.setIcon(QIcon("uploaded.png"))
        if not self.percentageBar_container:
            self.btn.setEnabled(True)

    @pyqtSlot(uuid.UUID, int)
    def handle_percentageChanged(self, identifier, percentage):
        percentageBar = self.percentageBar_container.get(identifier)
        if percentageBar is not None:
            percentageBar.setValue(percentage)


class S3Worker(QObject):
    started = pyqtSignal(uuid.UUID)
    finished = pyqtSignal(uuid.UUID)
    percentageChanged = pyqtSignal(uuid.UUID, int)

    def __init__(self, domain, awsID, awsSecret, parent=None):
        super().__init__(parent)
        self.domain = domain
        self.awsID = awsID
        self.awsSecret = awsSecret
        """self._s3 = boto3.client(
            "s3",
            endpoint_url=self.domain,
            aws_access_key_id=self.awsID,
            aws_secret_access_key=self.awsSecret,
        )"""
        self._seen_so_far = dict()

    @property
    def s3(self):
        return self._s3

    def upload(self, filename, bucketname, objectname, identifier):
        self._size = float(os.path.getsize(filename))
        self._seen_so_far[identifier] = 0
        threading.Thread(
            target=self._execute,
            args=(filename, bucketname, objectname, identifier),
            daemon=True,
        ).start()

    def _execute(self, fileName, bucketName, objectName, identifier):
        self.started.emit(identifier)
        self.s3.upload_file(
            fileName,
            bucketName,
            objectName,
            Callback=partial(self._callback, identifier),
        )
        self.finished.emit(identifier)

    def _callback(self, identifier, bytes_amount):
        self._seen_so_far[identifier] += bytes_amount
        percentage = (self._seen_so_far / self._size) * 100
        if percentage > 100:
            self.percentageChanged.emit(identifier, 100)
        else:
            self.percentageChanged.emit(identifier, math.floor(percentage))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    demo = AppDemo()
    demo.show()

    sys.exit(app.exec_())