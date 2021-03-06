import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *

from Ui_qt_A01 import Ui_Frm_baidu_pic1
from F_A01 import Tl_baidu_DownPic02

# 自己建一个mywindows类，Tl_baidu_DownPic02 是自己的类名。QtWidgets.QMainWindow：继承该类方法
class c_tl_a01(QtWidgets.QMainWindow):
   # __init__:析构函数，也就是类被创建后就会预先加载的项目。
   # 马上运行，这个方法可以用来对你的对象做一些你希望的初始化。
    def __init__(self, parent=None):
       # 这里需要重载一下mywindow，同时也包含了QtWidgets.QMainWindow的预加载项。
        super(c_tl_a01, self).__init__(parent)
        self.child=Ui_Frm_baidu_pic1()
        self.child.setupUi(self)
        self.child.btn_select.clicked.connect(self.sel_directory)
        self.child.btn_download.clicked.connect(self.baidu_dl_pic01)
        self.child.btn_open_path.clicked.connect(self.open_path)
        self.child.t_directory.setText('e://')
        self.child.t_pic_count.setText(str(10))

    def baidu_dl_pic01(self):
        pass
        t_keyword = self.child.t_baidu_Keyword.text()
        t_directory = self.child.t_directory.text()
        t_pic_count = self.child.t_pic_count.text()
        # print(t_keyword)
        # print(t_directory)
        # print(t_pic_count)
        if t_keyword == '' or t_directory == '' or t_pic_count == '':
            reply = QMessageBox.information(
                self, '提醒', '参数为空,请检查并补录完整', QMessageBox.Yes, QMessageBox.Yes)
        else:
            reply = QMessageBox.question(
                self, '确认', '是否要从Baidu下载图片,这将花费较长时间', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                print('下载')
                Tl_baidu_DownPic02(t_keyword,t_directory,int(t_pic_count))
                reply = QMessageBox.information(
                self, '提醒', '下载完成', QMessageBox.Yes, QMessageBox.Yes)
            else:
                print('不下载')

    def sel_directory(self):
        pass
        #     打开文件有以下3种：
        # 1、单个文件打开 QFileDialog.getOpenFileName()
        # 2、多个文件打开 QFileDialog.getOpenFileNames()
        # 3、打开文件夹 QFileDialog.getExistingDirectory()
        dir_path = QFileDialog.getExistingDirectory(self, "请选择文件夹路径", "/")
        print(dir_path)
        self.child.t_directory.setText(dir_path)
        # print(dir_path)

    def open_path(self):
        dir_path=self.child.t_directory.text()
        if os.path.exists(dir_path):
            os.startfile(dir_path)
        #     打开文件有以下3种：
        # 1、单个文件打开 QFileDialog.getOpenFileName()
        # 2、多个文件打开 QFileDialog.getOpenFileNames()
        # 3、打开文件夹 QFileDialog.getExistingDirectory()
        
if __name__ == '__main__':  # 如果整个程序是主程序
    # QApplication相当于main函数，也就是整个程序（很多文件）的主入口函数。
    # 对于GUI程序必须至少有一个这样的实例来让程序运行。
    app = QtWidgets.QApplication(sys.argv)
    # 生成 mywindow 类的实例。
    window =c_tl_a01()
    # 有了实例，就得让它显示，show()是QWidget的方法，用于显示窗口。
    window.show()

    # 调用sys库的exit退出方法，条件是app.exec_()，也就是整个窗口关闭。
    # 有时候退出程序后，sys.exit(app.exec_())会报错，改用app.exec_()就没事
    # https://stackoverflow.com/questions/25719524/difference-between-sys-exitapp-exec-and-app-exec
    sys.exit(app.exec_())
