# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hello.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelloWoldDialog(object):
    def setupUi(self, HelloWoldDialog):
        HelloWoldDialog.setObjectName("HelloWoldDialog")
        HelloWoldDialog.resize(400, 300)
        self.label = QtWidgets.QLabel(HelloWoldDialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 91, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(HelloWoldDialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 241, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.Button_OK = QtWidgets.QPushButton(HelloWoldDialog)
        self.Button_OK.setGeometry(QtCore.QRect(280, 140, 61, 41))
        self.Button_OK.setObjectName("Button_OK")
        self.label_result = QtWidgets.QLabel(HelloWoldDialog)
        self.label_result.setGeometry(QtCore.QRect(40, 160, 111, 41))
        self.label_result.setObjectName("label_result")

        self.retranslateUi(HelloWoldDialog)
        QtCore.QMetaObject.connectSlotsByName(HelloWoldDialog)

    def retranslateUi(self, HelloWoldDialog):
        _translate = QtCore.QCoreApplication.translate
        HelloWoldDialog.setWindowTitle(_translate("HelloWoldDialog", "Dialog"))
        self.label.setText(_translate("HelloWoldDialog", "Enter your Name"))
        self.Button_OK.setText(_translate("HelloWoldDialog", "OK"))
        self.label_result.setText(_translate("HelloWoldDialog", "X"))
        self.Button_OK.clicked.connect(self.button_pressed)

    def button_pressed(self):
        self.label_result.setText("Hello" + self.lineEdit.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelloWoldDialog = QtWidgets.QDialog()
    ui = Ui_HelloWoldDialog()
    ui.setupUi(HelloWoldDialog)
    HelloWoldDialog.show()
    sys.exit(app.exec_())

