pyrcc5 default.qrc -o default_rc.py

https://www.riverbankcomputing.com/static/Docs/PyQt5/designer.html#pyuic5
pyuic5.exe .\dynamic.ui -o .\dynamic_ui.py
uic.loadUi(os.path.join(MisConf.UI_PATH, 'common','attach.ui'), self)


form_class = uic.loadUiType(os.path.join(MisConf.UI_PATH, 'common', 'gridfind.ui'))[0]
class GridFind(QtWidgets.QDialog, form_class):

https://www.riverbankcomputing.com/software/sip/intro
https://www.ics.uci.edu/~dock/manuals/sip/sipref.html
https://en.wikipedia.org/wiki/SIP_(software)
SIP - A Tool for Generating Python Bindings for C and C++ Libraries
