#https://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object-instance

#class 및 생성된 하위 instance에 메소드 추가
#p
class A:
    def __init__(self):
        self.no = 1

    def prt1(self):
        print( 'prt1:', self.no )

a1 = A()
a2 = A()

a1.prt1()
a2.prt1()

try:
    a1.prt2()
except Exception as e:
    print('err', e)

a2.prt1()

def prt2(self):
    print('prt2:', self.no)

A.prt2 = prt2 #A 클래스와 하위 instance 전체에 prt2 메소드 추가
print( dir(A), dir(a1), dir(a2) )
a1.prt2()
a2.prt2()


#a2 인스턴스에 메소드 추가하기
def prt3(self):
    print('prt3:', self.no)

a1.prt3 = prt3
try:
    a1.prt3()
except Exception as e:
    print('instance와 self가 바인딩이 안됨', e)

import types
a1.prt3 = types.MethodType(prt3, a1)

a1.prt3()

try:
    a2.prt3()
except Exception as e:
    print('a1 instance에만 추가됨, a2에는 없음', e)

print( dir(A), dir(a1), dir(a2) )


from PyQt5 import QtWidgets

def my_prt(self):
    print('self.objectName()')

QtWidgets.QWidget.my_prt = my_prt

app = QtWidgets.QApplication([])
win = QtWidgets.QWidget()
win.my_prt()
win.show()
app.exec()
