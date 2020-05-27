import sys
from PyQt5.QtCore import QObject, pyqtSlot, pyqtProperty, pyqtSignal 
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage


class HelloWorldHtmlApp(QWebEngineView):
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8"/>        
        <script src="qrc:///qtwebchannel/qwebchannel.js"></script>
        <script>
        var backend;
        new QWebChannel(qt.webChannelTransport, function (channel) {
            backend = channel.objects.backend;
        });
        </script>
    </head>
    <body> <h2>HTML loaded.</h2> </body>
    </html>
    '''

    def __init__(self):
        super().__init__()

        # setup a page with my html
        my_page = QWebEnginePage(self)
        my_page.setHtml(self.html)
        self.setPage(my_page)

        # setup channel
        self.channel = QWebChannel()
        self.backend = self.Backend(self)
        self.channel.registerObject('backend', self.backend)
        self.page().setWebChannel(self.channel)

    class Backend(QObject):
        """ Container for stuff visible to the JavaScript side. """
        foo_changed = pyqtSignal(str)

        def __init__(self, htmlapp):
            super().__init__()
            self.htmlapp = htmlapp
            self._foo = "Hello World"

        @pyqtSlot()
        def debug(self):
            self.foo = "I modified foo!"

        @pyqtProperty(str, notify=foo_changed)
        def foo(self):            
            return self._foo

        @foo.setter
        def foo(self, new_foo):            
            self._foo = new_foo
            self.foo_changed.emit(new_foo)


if __name__ == "__main__":
    app = QApplication(['--no-sandbox','--no-sandbox',])
    view = HelloWorldHtmlApp()
    view.show()
    app.exec_()