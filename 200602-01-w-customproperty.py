# https://stackoverflow.com/questions/30652828/add-custom-attribute-to-qcheckbox-widget

# 상속 방식
# setProperty() #https://wiki.qt.io/Dynamic_Properties_and_Stylesheets
# 기본 속성 추가

import inspect

import sys
from PyQt5 import QtWidgets, QtGui

# 상속 방식
class MyCheckBox(QtWidgets.QCheckBox):
    def __init__(self, my_param, *args, **kwargs):
        QtWidgets.QCheckBox.__init__(self, *args, **kwargs)
        self.custom_param = my_param



app = QtWidgets.QApplication([])
cb = MyCheckBox('1')
cb.resize(100, 100)
cb.show()
print('custom_param', cb.custom_param )

cb1 = QtWidgets.QCheckBox()
cb1.setProperty('next_param', 'hello')
print('next_param', cb1.property( 'next_param' ) )
try:
    #print('next_param', cb1.property( 'next_param' ) )
    print('custom_param', cb.property( 'custom_param' ) )
    print('cb1.next_param', cb1.next_param )
except:
    pass


cb2 = QtWidgets.QCheckBox()
cb2.attr1 = '@??'
print( 'cb2.attr1', cb2.attr1 )

try:
    print( 'cb1.attr1', cb1.attr1 )
    print( 'custom_param',  cb2.attr1, '?++' )
    print( 'cb2.attr1', cb2.attr1 )
except:
    pass


app.exec()
