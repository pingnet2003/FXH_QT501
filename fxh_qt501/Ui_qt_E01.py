# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\vscode_2020\vstestfxh\fxh_qt501\fxh_qt501\qt_E01.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frm_Excel_Import(object):
    def setupUi(self, Frm_Excel_Import):
        Frm_Excel_Import.setObjectName("Frm_Excel_Import")
        Frm_Excel_Import.resize(655, 388)
        self.frame = QtWidgets.QFrame(Frm_Excel_Import)
        self.frame.setGeometry(QtCore.QRect(20, 10, 551, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 20, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 91, 20))
        self.label_2.setObjectName("label_2")
        self.t_directory = QtWidgets.QLineEdit(self.frame)
        self.t_directory.setGeometry(QtCore.QRect(110, 60, 371, 20))
        self.t_directory.setObjectName("t_directory")
        self.t_db_name = QtWidgets.QLineEdit(self.frame)
        self.t_db_name.setGeometry(QtCore.QRect(110, 20, 371, 20))
        self.t_db_name.setObjectName("t_db_name")
        self.btn_select = QtWidgets.QPushButton(self.frame)
        self.btn_select.setGeometry(QtCore.QRect(480, 60, 31, 23))
        self.btn_select.setObjectName("btn_select")
        self.btn_import = QtWidgets.QPushButton(self.frame)
        self.btn_import.setGeometry(QtCore.QRect(345, 100, 75, 23))
        self.btn_import.setObjectName("btn_import")
        self.btn_Close = QtWidgets.QPushButton(self.frame)
        self.btn_Close.setGeometry(QtCore.QRect(420, 100, 75, 23))
        self.btn_Close.setObjectName("btn_Close")

        self.retranslateUi(Frm_Excel_Import)
        self.btn_Close.clicked.connect(Frm_Excel_Import.close)
        QtCore.QMetaObject.connectSlotsByName(Frm_Excel_Import)

    def retranslateUi(self, Frm_Excel_Import):
        _translate = QtCore.QCoreApplication.translate
        Frm_Excel_Import.setWindowTitle(_translate("Frm_Excel_Import", "Excel 导入"))
        self.label.setText(_translate("Frm_Excel_Import", "DB Name"))
        self.label_2.setText(_translate("Frm_Excel_Import", "Excel文件路径"))
        self.btn_select.setText(_translate("Frm_Excel_Import", "..."))
        self.btn_import.setText(_translate("Frm_Excel_Import", "导入"))
        self.btn_Close.setText(_translate("Frm_Excel_Import", "退出"))
