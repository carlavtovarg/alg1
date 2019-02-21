# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListManager.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ListaManager(object):
    def setupUi(self, ListaManager):
        ListaManager.setObjectName("ListaManager")
        ListaManager.resize(577, 427)
        self.centralwidget = QtWidgets.QWidget(ListaManager)
        self.centralwidget.setObjectName("centralwidget")
        self.edit_add = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_add.setGeometry(QtCore.QRect(40, 40, 211, 20))
        self.edit_add.setObjectName("edit_add")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 90, 211, 23))
        self.pushButton.setObjectName("pushButton")
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(40, 330, 221, 23))
        self.Clear.setObjectName("Clear")
        self.listItems = QtWidgets.QListWidget(self.centralwidget)
        self.listItems.setGeometry(QtCore.QRect(290, 30, 256, 321))
        self.listItems.setObjectName("listItems")
        ListaManager.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ListaManager)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 21))
        self.menubar.setObjectName("menubar")
        ListaManager.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ListaManager)
        self.statusbar.setObjectName("statusbar")
        ListaManager.setStatusBar(self.statusbar)

        self.retranslateUi(ListaManager)
        QtCore.QMetaObject.connectSlotsByName(ListaManager)

        self.pushButton.clicked.connect(self.add_element)
        self.Clear.clicked.connect(self.clear_list)

    def add_element(self):
        new_element = self.edit_add.text()

        self.listItems.addItem(new_element)

    def clear_list(self):
        self.listItems.clear()



    def retranslateUi(self, ListaManager):
        _translate = QtCore.QCoreApplication.translate
        ListaManager.setWindowTitle(_translate("ListaManager", "MainWindow"))
        self.pushButton.setText(_translate("ListaManager", "Add Row"))
        self.Clear.setText(_translate("ListaManager", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ListaManager = QtWidgets.QMainWindow()
    ui = Ui_ListaManager()
    ui.setupUi(ListaManager)
    ListaManager.show()
    sys.exit(app.exec_())

