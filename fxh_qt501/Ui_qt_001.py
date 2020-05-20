# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\vscode_2020\vstestfxh\fxh_qt501\fxh_qt501\qt_001.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_qt001(object):
    def setupUi(self, qt001):
        qt001.setObjectName("qt001")
        qt001.resize(720, 595)
        self.label = QtWidgets.QLabel(qt001)
        self.label.setGeometry(QtCore.QRect(20, 30, 54, 12))
        self.label.setObjectName("label")
        self.t_file = QtWidgets.QLineEdit(qt001)
        self.t_file.setGeometry(QtCore.QRect(80, 30, 481, 20))
        self.t_file.setObjectName("t_file")
        self.btn_select_file = QtWidgets.QPushButton(qt001)
        self.btn_select_file.setGeometry(QtCore.QRect(560, 30, 31, 23))
        self.btn_select_file.setObjectName("btn_select_file")
        self.btn_read = QtWidgets.QPushButton(qt001)
        self.btn_read.setGeometry(QtCore.QRect(590, 30, 75, 23))
        self.btn_read.setObjectName("btn_read")
        self.btn_cloud = QtWidgets.QPushButton(qt001)
        self.btn_cloud.setGeometry(QtCore.QRect(30, 310, 75, 23))
        self.btn_cloud.setObjectName("btn_cloud")
        self.gv_pic = QtWidgets.QGraphicsView(qt001)
        self.gv_pic.setGeometry(QtCore.QRect(50, 340, 581, 241))
        self.gv_pic.setObjectName("gv_pic")
        self.te_text = QtWidgets.QTextEdit(qt001)
        self.te_text.setGeometry(QtCore.QRect(30, 70, 631, 231))
        self.te_text.setObjectName("te_text")

        self.retranslateUi(qt001)
        QtCore.QMetaObject.connectSlotsByName(qt001)

    def retranslateUi(self, qt001):
        _translate = QtCore.QCoreApplication.translate
        qt001.setWindowTitle(_translate("qt001", "词云01"))
        self.label.setText(_translate("qt001", "文件路径"))
        self.btn_select_file.setText(_translate("qt001", "..."))
        self.btn_read.setText(_translate("qt001", "Read"))
        self.btn_cloud.setText(_translate("qt001", "生成词云"))
