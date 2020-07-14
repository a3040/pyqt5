# https://stackoverflow.com/questions/62823772/check-if-user-clicked-bolded-text-in-qtextbrowser
# 마우스가 textbrowser 의 특정 위치에 존재하는가?

import sys
from PyQt5 import QtGui, QtWidgets


class TextBrowser(QtWidgets.QTextBrowser):
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        pos = event.pos()
        tc = self.cursorForPosition(pos)
        fmt = tc.charFormat()
        if fmt.fontWeight() == QtGui.QFont.Bold:
            print("text:", tc.block().text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = TextBrowser()

    html = """
    <!DOCTYPE html>
        <html>
            <body>

            <p>This text is normal.</p>
            <p><b>This text is bold.</b></p>
            <p><strong>This text is important!</strong></p>
            <p><i>This text is italic</i></p>
            <p><em>This text is emphasized</em></p>
            <p><small>This is some smaller text.</small></p>
            <p>This is <sub>subscripted</sub> text.</p>
            <p>This is <sup>superscripted</sup> text.</p>
            </body>
        </html>
    """

    w.insertHtml(html)

    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())