import sys
import time
import os
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets
# from PyQt5.QtWidgets import QTableWidget, QProgressBar, QLineEdit, QComboBox, QFrame, QTableWidgetItem
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# 这个test_pyqt是ui文件对应的py文件的文件名
from Ui_qt_001 import Ui_qt001

import wordcloud   #pip install wordcloud
import jieba     #pip install jieba

#调用 QT 设计的界面对应的类
class W001(QDialog):
    def __init__(self, parent=None):        
        super(W001, self).__init__(parent)
        self.child = Ui_qt001()
        self.child.setupUi(self)
        self.child.btn_select_file.clicked.connect(self.select_file)
        self.child.btn_read.clicked.connect(self.Read_txt)
        self.child.btn_cloud.clicked.connect(self.gen_word_cloud)

    # 设立函数，来取得当前时间
    def get_sysdate(self):
        now = time.strftime("%Y%m%d %H%M%S", time.localtime(time.time()))
        # print(now)
        return now

    def select_file(self):
        fileName, filetype = QFileDialog.getOpenFileName(self, "选择文件", "/", "All Files (*);;TXT Files (*.txt)") # User 选择路径来找到图片
        # print(fileName, filetype)  # 打印文件全部路径（包括文件名和后缀名）和文件类型
        self.child.t_file.setText(fileName)    #把文件的路径写在 Text 上

    def Read_txt(self):
        filename=self.child.t_file.text()
        with open(filename,'r',encoding='GBK') as f:
            self.child.te_text.setText(f.read())
    
    def gen_word_cloud(self):
        #取得文件名
        filename=self.child.t_file.text()
        #分离出文件路径及文件名
        if filename=='':
            filepath='d://'
            tempfilename=self.get_sysdate()+'.png'
        else:
            (filepath,tempfilename)=os.path.split(filename)
            (tempfilename,extension)=os.path.splitext(tempfilename)
            tempfilename=tempfilename+self.get_sysdate()+'.png'
        file=os.path.join(filepath,tempfilename)
        self.child.t_aim_file.setText(file)
        # print(file)
        #以上完成文件名

        # 词云都是词语 显示      
        txt=self.child.te_text.toPlainText()  #获取内容
        # print(txt)

        w = wordcloud.WordCloud(width=1000,height=700,background_color='white',contour_width=1,font_path="C:/Windows/Fonts/STFANGSO.TTF")
        txt_list = jieba.lcut(txt)
        string = "".join(txt_list)
        # print(string)
        w.generate(string)
        w.to_file(file)

        #把file显示出来
        #显示图片
        self.child.lbl_pic.setPixmap(QPixmap(file))  # 在label上显示图片
        self.child.lbl_pic.setScaledContents (True) # 让图片自适应label大小

if __name__ == "__main__":    
    app = QApplication(sys.argv)
    my001 = W001()    
    my001.show()
    sys.exit(app.exec_())        