import sys
import time
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets
# from PyQt5.QtWidgets import QTableWidget, QProgressBar, QLineEdit, QComboBox, QFrame, QTableWidgetItem
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# 这个test_pyqt是ui文件对应的py文件的文件名
from Ui_qt_C02 import Ui_qt_c02

from PIL import ImageGrab  # pip3 install pillow
import numpy as np    # pip3 install numpy
import cv2             # pip3 install opencv-python
import datetime
from pynput import keyboard   # pip3 install pynput
import threading

flag = False  # 停止标志位

# 调用 QT 设计的界面对应的类


class BackendThread(QObject):
    # 通过类成员对象定义信号
    update_date = pyqtSignal(str)

    # 处理业务逻辑
    def run(self):
        for i in range(10, 0, -1):
            self.update_date.emit(str(i))
            time.sleep(1)


class WC02(QDialog):
    def __init__(self, parent=None):
        super(WC02, self).__init__(parent)
        self.child = Ui_qt_c02()
        self.child.setupUi(self)
        self.child.btn_start.clicked.connect(self.start_screen)
        self.child.btn_select.clicked.connect(self.sel_directory)
        self.child.btn_open_path.clicked.connect(self.open_path)

        self.child.btn_countDown.clicked.connect(self.start_down)

    def start_down(self):
        # for i in range(10, 0, -1):
        #     self.child.lbl_digit.setText(str(i))
        #     time.sleep(1)
        # 创建线程
        self.backend = BackendThread()
        # 连接信号
        self.backend.update_date.connect(self.handleDisplay)
        self.thread = QThread()
        self.backend.moveToThread(self.thread)
        # 开始线程
        self.thread.started.connect(self.backend.run)
        self.thread.start()

    # 将当前时间输出到文本框
    def handleDisplay(self, data):
        self.child.lbl_digit.setText(data)

    # 设立函数，来取得当前时间

    def get_sysdate(self):
        now = time.strftime("%Y%m%d %H%M%S", time.localtime(time.time()))
        # print(now)
        return now

    def sel_directory(self):
        pass
        #     打开文件有以下3种：
        # 1、单个文件打开 QFileDialog.getOpenFileName()
        # 2、多个文件打开 QFileDialog.getOpenFileNames()
        # 3、打开文件夹 QFileDialog.getExistingDirectory()
        dir_path = QFileDialog.getExistingDirectory(self, "请选择文件夹路径", "/")
        # print(dir_path)
        self.child.t_directory.setText(dir_path)

    def video_record(self):
        # """
        # 屏幕录制！
        # :return:
        # """
        name = self.get_sysdate()+'.avi'  # 当前的时间
        t_directory = self.child.t_directory.text()  # 新生成文件， 要保存的文件夹
        if t_directory == '':
            pass
        else:
            new_file_name = os.path.join(t_directory, name)  # 新生成的文件，含路径
            # print(new_file_name)

            p = ImageGrab.grab()  # 获得当前屏幕
            a, b = p.size  # 获得当前屏幕的大小
            # 编码格式   常用的有 “DIVX"、”MJPG"、“XVID”、“X264"
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            # 输出文件 帧率为16，可以自己设置
            # VideoWriter(filename, fourcc, fps, frameSize[, isColor]) -> <VideoWriter object>
            # 第一个参数是要保存的文件的路径
            # fourcc 指定编码器
            # fps 要保存的视频的帧率，本例为 20fps (frame per second)
            # frameSize 要保存的文件的画面尺寸,本例为 当前屏幕的大小
            # isColor 指示是黑白画面还是彩色的画面
            video = cv2.VideoWriter(new_file_name, fourcc, 20, (a, b))
            while True:
                im = ImageGrab.grab()
                # CvtColor是Opencv里的 转换图像的颜色空间
                # cvtColor(src, code, dst=None, dstCn=None)
                # src: 原图像； code: 指定颜色空间转换类型；
                # dst: 目标图像；与原图像大小深度一致；dstCn: 指定目标图像通道数；默认None，则会根据src、code自动计算；
                # https://www.cnblogs.com/chenzhen0530/p/10741264.html 有说明
                # 转为opencv的BGR格式
                imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
                video.write(imm)
                if flag:
                    print("录制结束！")
                    break
            video.release()

    def on_press(self, key):
        # """
        # 键盘监听事件！！！
        # :param key:
        # :return:
        # """
        # print(key)
        global flag
        if key == keyboard.Key.esc:
            flag = True
            print("stop monitor！")
            return False  # 返回False，键盘监听结束！

    def start_screen(self):
        pass
        t_directory = self.child.t_directory.text()  # 新生成文件， 要保存的文件夹
        if t_directory == '':
            pass
            reply = QMessageBox.information(
                self, '提醒', '请先选择 输出文件夹', QMessageBox.Yes, QMessageBox.Yes)
        else:
            reply = QMessageBox.information(
                self, '提醒', '准备开始录制... 按ESC 结束录制', QMessageBox.Yes, QMessageBox.Yes)
            # self.start_down()
            th = threading.Thread(target=self.video_record)
            th.start()
            with keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()
            reply = QMessageBox.information(
                self, '提醒', '已录制完毕', QMessageBox.Yes, QMessageBox.Yes)

    def open_path(self):
        dir_path = self.child.t_directory.text()
        if os.path.exists(dir_path):
            os.startfile(dir_path)
        #     打开文件有以下3种：
        # 1、单个文件打开 QFileDialog.getOpenFileName()
        # 2、多个文件打开 QFileDialog.getOpenFileNames()
        # 3、打开文件夹 QFileDialog.getExistingDirectory()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myc02 = WC02()
    myc02.show()
    sys.exit(app.exec_())
