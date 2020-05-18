import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtGui, QtCore, QtWidgets
# from PyQt5.QtWidgets import QTableWidget, QProgressBar, QLineEdit, QComboBox, QFrame, QTableWidgetItem
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# 这个 Ui_Tl_Split_Pic01 是ui文件对应的py文件的文件名
from Ui_Tl_Split_Pic01 import Ui_Form_Split_Pic
from Fun_Split_Pic9 import *    #调用自编的函数来分割
import os
import time

# 我的Form是用的QWidget作为基类
class MyWindow(QWidget, Ui_Form_Split_Pic):    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_select_pic.clicked.connect(self.select_pic)        
        self.btn_split9.clicked.connect(self.split_pic9)
        self.btn_open.clicked.connect(self.open_dir)    

    # 设立函数，来取得当前时间
    def get_sysdate(self):
        now = time.strftime("%Y%m%d %H%M%S", time.localtime(time.time()))
        # print(now)
        return now

    def select_pic(self):
        fileName, filetype = QFileDialog.getOpenFileName(self, "选择文件", "/", "All Files (*);;PNG Files (*.png)") # User 选择路径来找到图片
        print(fileName, filetype)  # 打印文件全部路径（包括文件名和后缀名）和文件类型
        self.t_pic_path.setText(fileName)    #把图片的路径写在 Text 上
        self.l_pic_orig.setPixmap(QPixmap(fileName))  # 在label上显示图片
        self.l_pic_orig.setScaledContents (True) # 让图片自适应label大小

    def open_dir(self):
        new_dir=self.l_new_dir.text()
        os.startfile(new_dir)  # 打开目录
       
    #把图片切割成九宫格格式
    def split_pic9(self):
        #取得要切割的图片文件名及路径
        yy = self.t_pic_path.text()        
        # 分离出文件所在的路径
        (file_dir, tempfilename) = os.path.split(yy)
        # 分离出文件的名字和后缀:
        (filename, extension) = os.path.splitext(tempfilename)
        #分离出的文件保存路径
        new_dir = os.path.join(file_dir,filename+'-'+self.get_sysdate())
        #创建路径
        os.makedirs(new_dir)

        self.l_new_dir.setText(new_dir)    #把图片的路径写在 Text 上        

        #把图片切割成九宫格格式
        Start_split(yy,new_dir)
        
        #显示图片
        self.l_pic_01.setPixmap(QPixmap(os.path.join(new_dir,'1.png')))  # 在label上显示图片
        self.l_pic_01.setScaledContents (True) # 让图片自适应label大小

        self.l_pic_02.setPixmap(QPixmap(os.path.join(new_dir,'2.png')))  # 在label上显示图片
        self.l_pic_02.setScaledContents (True) # 让图片自适应label大小

        self.l_pic_03.setPixmap(QPixmap(os.path.join(new_dir,'3.png')))  # 在label上显示图片
        self.l_pic_03.setScaledContents (True) # 让图片自适应label大小

        self.l_pic_04.setPixmap(QPixmap(os.path.join(new_dir,'4.png')))  # 在label上显示图片
        self.l_pic_04.setScaledContents (True) # 让图片自适应label大小

        self.l_pic_05.setPixmap(QPixmap(os.path.join(new_dir,'5.png')))  # 在label上显示图片
        self.l_pic_05.setScaledContents (True) # 让图片自适应label大小

        self.l_pic_06.setPixmap(QPixmap(os.path.join(new_dir,'6.png')))  # 在label上显示图片
        self.l_pic_06.setScaledContents (True) # 让图片自适应label大小

        self.l_pic_07.setPixmap(QPixmap(os.path.join(new_dir,'7.png')))  # 在label上显示图片
        self.l_pic_07.setScaledContents (True) # 让图片自适应label大小

        self.l_pic_08.setPixmap(QPixmap(os.path.join(new_dir,'8.png')))  # 在label上显示图片
        self.l_pic_08.setScaledContents (True) # 让图片自适应label大小

        self.l_pic_09.setPixmap(QPixmap(os.path.join(new_dir,'9.png')))  # 在label上显示图片
        self.l_pic_09.setScaledContents (True) # 让图片自适应label大小

        reply = QMessageBox.information(self, '提示','成功切割图片',QMessageBox.Yes,QMessageBox.Yes)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.resize(900, 800)
    w.show()
    sys.exit(app.exec_())