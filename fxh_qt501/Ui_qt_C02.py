# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\vscode_2020\vstestfxh\fxh_qt501\fxh_qt501\qt_C02.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_qt_c02(object):
    def setupUi(self, qt_c02):
        qt_c02.setObjectName("qt_c02")
        qt_c02.resize(726, 300)
        self.btn_start = QtWidgets.QPushButton(qt_c02)
        self.btn_start.setGeometry(QtCore.QRect(70, 70, 121, 23))
        self.btn_start.setObjectName("btn_start")
        self.btn_exit = QtWidgets.QPushButton(qt_c02)
        self.btn_exit.setGeometry(QtCore.QRect(70, 150, 121, 23))
        self.btn_exit.setObjectName("btn_exit")
        self.t_directory = QtWidgets.QLineEdit(qt_c02)
        self.t_directory.setGeometry(QtCore.QRect(110, 20, 371, 20))
        self.t_directory.setObjectName("t_directory")
        self.label_2 = QtWidgets.QLabel(qt_c02)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 71, 16))
        self.label_2.setObjectName("label_2")
        self.btn_select = QtWidgets.QPushButton(qt_c02)
        self.btn_select.setGeometry(QtCore.QRect(480, 20, 31, 23))
        self.btn_select.setObjectName("btn_select")
        self.btn_open_path = QtWidgets.QPushButton(qt_c02)
        self.btn_open_path.setGeometry(QtCore.QRect(70, 110, 121, 23))
        self.btn_open_path.setObjectName("btn_open_path")

        self.retranslateUi(qt_c02)
        self.btn_exit.clicked.connect(qt_c02.close)
        QtCore.QMetaObject.connectSlotsByName(qt_c02)

    def retranslateUi(self, qt_c02):
        _translate = QtCore.QCoreApplication.translate
        qt_c02.setWindowTitle(_translate("qt_c02", "录屏软件"))
        self.btn_start.setText(_translate("qt_c02", "开始录屏"))
        self.btn_exit.setText(_translate("qt_c02", "关闭程序"))
        self.label_2.setText(_translate("qt_c02", "文件夹路径"))
        self.btn_select.setText(_translate("qt_c02", "..."))
        self.btn_open_path.setText(_translate("qt_c02", "打开下载目录"))
