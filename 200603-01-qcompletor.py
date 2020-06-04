# https://stackoverflow.com/questions/62162443/multicolumn-model-for-qcompleter
# 자동완성

from PyQt5.QtCore import pyqtSlot, QObject
from PyQt5.QtWidgets import (QApplication, QMainWindow, QComboBox,
                             QCompleter, QTableView, QLabel)
from PyQt5.QtSql import (QSqlQuery, QSqlQueryModel, QSqlDatabase)
import sys
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        self.setGeometry(300, 300, 400, 300)

        fid = open('example.db', 'w')
        fid.close()

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('example.db')
        db.open()
        query = QSqlQuery(db)

        query.exec_('CREATE TABLE "airports" ("city" TEXT, "code" TEXT)')

        airports = [('Aberdeen, SD','ABR'), ('Abilene, TX','ABI'),
                    ('Adak Island, AK','ADK'), ('Akiachak, AK','KKI'),
                    ('Akiak, AK','AKI'), ('Akron/Canton, OH','CAK'),
                    ('Akuton, AK','KQA'), ('Alakanuk, AK','AUK'),
                    ('Alamogordo, NM','ALM'), ('Alamosa, CO','ALS'),
                    ('Albany, NY','ALB'), ('Albuquerque, NM','ABQ')]
        for item in airports:
            sql = 'INSERT INTO airports(city, code) VALUES(?, ?)'
            query.prepare(sql)
            query.addBindValue(item[0])
            query.addBindValue(item[1])
            query.exec_()

        query.exec_('SELECT * FROM airports')

        model =  QSqlQueryModel()
        model.setQuery(query)

        self.cb = QComboBox(parent = self)
        self.cb.setModel(model)
        self.cb.setModelColumn(1)
        self.cb.setView(QTableView(self.cb))
        self.cb.setGeometry(50,50, 250, 50)
        self.cb.currentIndexChanged.connect(self.indexer)

        self.label = QLabel(parent = self)
        self.label.setGeometry(20,200, 250, 50)

        self.cb.view().setMinimumWidth(500)
        self.cb.setEditable(True)

        self.completer = QCompleter()
        self.completer.setCaseSensitivity(False)
        self.cb.setCompleter(self.completer)
        self.completer.setModel(model)
        self.completer.setCompletionColumn(1)
        self.completer.setPopup(QTableView())
        self.completer.popup().setMinimumWidth(500)
        self.completer.popup().setMinimumHeight(500)

        self.completer.activated.connect(self.activatedHandler)

    #@pyqtSlot(QObject)        
    def activatedHandler(self, arg):
        pass

    def indexer(self, idx):
        self.label.setText('%d' % idx)

app = QApplication(sys.argv)
main = MainWindow(None)
main.show()
sys.exit(app.exec_())