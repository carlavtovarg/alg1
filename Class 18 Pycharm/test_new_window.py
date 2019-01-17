import sys
from PyQt5 import QtCore, QtGui, QtWidgets


def window():

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setGeometry(50,50,500,500)
    window.setWindowTitle("Hello")
    window.show()
    sys.exc_info(app.exec_())


window()

