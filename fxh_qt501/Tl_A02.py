import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *

from Ui_qt_A02 import Ui_Frm_youget_video

# 需要安装you-get,安装方法: pip install you-get


# 自己建一个mywindows类，QtWidgets.QMainWindow：继承该类方法
class c_tl_a02(QtWidgets.QMainWindow):
   # __init__:析构函数，也就是类被创建后就会预先加载的项目。
   # 马上运行，这个方法可以用来对你的对象做一些你希望的初始化。
    def __init__(self, parent=None):
       # 这里需要重载一下mywindow，同时也包含了QtWidgets.QMainWindow的预加载项。
        super(c_tl_a02, self).__init__(parent)
        self.child=Ui_Frm_youget_video()
        self.child.setupUi(self)
        self.child.btn_select.clicked.connect(self.sel_directory)
        self.child.btn_download.clicked.connect(self.youget_dl_video01)
        self.child.btn_open_path.clicked.connect(self.open_path)
        self.child.t_directory.setText('e://')
        
    def youget_dl_video01(self):
        pass
        t_website = self.child.t_youget_website.text()
        t_directory = self.child.t_directory.text()        
        # print(t_keyword)
        # print(t_directory)
        # print(t_pic_count)
        if t_website == '' or t_directory == '' :
            reply = QMessageBox.information(
                self, '提醒', '参数为空,请检查并补录完整', QMessageBox.Yes, QMessageBox.Yes)
        else:
            reply = QMessageBox.question(
                self, '确认', '是否要用 you-get 下载视频,这将花费较长时间', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                print('下载')
                command='you-get -o '+t_directory + '  '+ t_website
                print(command)
                os.system(command)
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
    window =c_tl_a02()
    # 有了实例，就得让它显示，show()是QWidget的方法，用于显示窗口。
    window.show()

    # 调用sys库的exit退出方法，条件是app.exec_()，也就是整个窗口关闭。
    # 有时候退出程序后，sys.exit(app.exec_())会报错，改用app.exec_()就没事
    # https://stackoverflow.com/questions/25719524/difference-between-sys-exitapp-exec-and-app-exec
    sys.exit(app.exec_())
