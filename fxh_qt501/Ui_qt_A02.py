# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\vscode_2020\vstestfxh\fxh_qt501\fxh_qt501\qt_A02.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frm_youget_video(object):
    def setupUi(self, Frm_youget_video):
        Frm_youget_video.setObjectName("Frm_youget_video")
        Frm_youget_video.resize(655, 388)
        self.frame = QtWidgets.QFrame(Frm_youget_video)
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
        self.t_youget_website = QtWidgets.QLineEdit(self.frame)
        self.t_youget_website.setGeometry(QtCore.QRect(110, 20, 371, 20))
        self.t_youget_website.setObjectName("t_youget_website")
        self.btn_select = QtWidgets.QPushButton(self.frame)
        self.btn_select.setGeometry(QtCore.QRect(480, 60, 31, 23))
        self.btn_select.setObjectName("btn_select")
        self.btn_download = QtWidgets.QPushButton(self.frame)
        self.btn_download.setGeometry(QtCore.QRect(110, 94, 75, 23))
        self.btn_download.setObjectName("btn_download")
        self.btn_Close = QtWidgets.QPushButton(self.frame)
        self.btn_Close.setGeometry(QtCore.QRect(290, 94, 75, 23))
        self.btn_Close.setObjectName("btn_Close")
        self.btn_open_path = QtWidgets.QPushButton(self.frame)
        self.btn_open_path.setGeometry(QtCore.QRect(190, 94, 91, 23))
        self.btn_open_path.setObjectName("btn_open_path")

        self.retranslateUi(Frm_youget_video)
        self.btn_Close.clicked.connect(Frm_youget_video.close)
        self.btn_select.clicked.connect(Frm_youget_video.sel_directory)        
        QtCore.QMetaObject.connectSlotsByName(Frm_youget_video)

    def retranslateUi(self, Frm_youget_video):
        _translate = QtCore.QCoreApplication.translate
        Frm_youget_video.setWindowTitle(_translate("Frm_youget_video", "视频下载(You-get 方式)"))
        self.label.setText(_translate("Frm_youget_video", "视频地址"))
        self.label_2.setText(_translate("Frm_youget_video", "文件夹路径"))
        self.btn_select.setText(_translate("Frm_youget_video", "..."))
        self.btn_download.setText(_translate("Frm_youget_video", "下载"))
        self.btn_Close.setText(_translate("Frm_youget_video", "退出"))
        self.btn_open_path.setText(_translate("Frm_youget_video", "打开下载目录"))
