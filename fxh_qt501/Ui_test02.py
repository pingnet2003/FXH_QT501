# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\vscode_2020\vstestfxh\fxh_qt501\fxh_qt501\test02.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_test_form1(object):
    def setupUi(self, test_form1):
        test_form1.setObjectName("test_form1")
        test_form1.resize(857, 345)
        self.btn_read = QtWidgets.QPushButton(test_form1)
        self.btn_read.setGeometry(QtCore.QRect(110, 30, 75, 23))
        self.btn_read.setObjectName("btn_read")
        self.TW_01 = QtWidgets.QTableWidget(test_form1)
        self.TW_01.setGeometry(QtCore.QRect(20, 90, 801, 201))
        self.TW_01.setObjectName("TW_01")
        self.TW_01.setColumnCount(0)
        self.TW_01.setRowCount(0)

        self.retranslateUi(test_form1)
        self.btn_read.clicked.connect(test_form1.p_readData)
        QtCore.QMetaObject.connectSlotsByName(test_form1)

    def retranslateUi(self, test_form1):
        _translate = QtCore.QCoreApplication.translate
        test_form1.setWindowTitle(_translate("test_form1", "Tests..."))
        self.btn_read.setText(_translate("test_form1", "Read Data"))
