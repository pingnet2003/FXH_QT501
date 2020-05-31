# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\vscode_2020\vstestfxh\fxh_qt501\fxh_qt501\qt_A01.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frm_baidu_pic1(object):
    def setupUi(self, Frm_baidu_pic1):
        Frm_baidu_pic1.setObjectName("Frm_baidu_pic1")
        Frm_baidu_pic1.resize(655, 388)
        self.frame = QtWidgets.QFrame(Frm_baidu_pic1)
        self.frame.setGeometry(QtCore.QRect(20, 10, 551, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 20, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 71, 16))
        self.label_2.setObjectName("label_2")
        self.t_directory = QtWidgets.QLineEdit(self.frame)
        self.t_directory.setGeometry(QtCore.QRect(110, 60, 371, 20))
        self.t_directory.setObjectName("t_directory")
        self.t_baidu_Keyword = QtWidgets.QLineEdit(self.frame)
        self.t_baidu_Keyword.setGeometry(QtCore.QRect(110, 20, 371, 20))
        self.t_baidu_Keyword.setObjectName("t_baidu_Keyword")
        self.btn_select = QtWidgets.QPushButton(self.frame)
        self.btn_select.setGeometry(QtCore.QRect(480, 60, 31, 23))
        self.btn_select.setObjectName("btn_select")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 54, 12))
        self.label_3.setObjectName("label_3")
        self.t_pic_count = QtWidgets.QLineEdit(self.frame)
        self.t_pic_count.setGeometry(QtCore.QRect(110, 100, 113, 20))
        self.t_pic_count.setObjectName("t_pic_count")
        self.btn_download = QtWidgets.QPushButton(self.frame)
        self.btn_download.setGeometry(QtCore.QRect(240, 100, 75, 23))
        self.btn_download.setObjectName("btn_download")
        self.btn_Close = QtWidgets.QPushButton(self.frame)
        self.btn_Close.setGeometry(QtCore.QRect(420, 100, 75, 23))
        self.btn_Close.setObjectName("btn_Close")
        self.btn_open_path = QtWidgets.QPushButton(self.frame)
        self.btn_open_path.setGeometry(QtCore.QRect(320, 100, 91, 23))
        self.btn_open_path.setObjectName("btn_open_path")

        self.retranslateUi(Frm_baidu_pic1)
        self.btn_Close.clicked.connect(Frm_baidu_pic1.close)
        self.btn_select.clicked.connect(Frm_baidu_pic1.sel_directory)
        self.btn_download.clicked.connect(Frm_baidu_pic1.baidu_dl_pic01)
        QtCore.QMetaObject.connectSlotsByName(Frm_baidu_pic1)

    def retranslateUi(self, Frm_baidu_pic1):
        _translate = QtCore.QCoreApplication.translate
        Frm_baidu_pic1.setWindowTitle(_translate("Frm_baidu_pic1", "Baidu 图片下载"))
        self.label.setText(_translate("Frm_baidu_pic1", "图片 关键词"))
        self.label_2.setText(_translate("Frm_baidu_pic1", "文件夹路径"))
        self.btn_select.setText(_translate("Frm_baidu_pic1", "..."))
        self.label_3.setText(_translate("Frm_baidu_pic1", "图片数量"))
        self.btn_download.setText(_translate("Frm_baidu_pic1", "下载"))
        self.btn_Close.setText(_translate("Frm_baidu_pic1", "退出"))
        self.btn_open_path.setText(_translate("Frm_baidu_pic1", "打开下载目录"))
