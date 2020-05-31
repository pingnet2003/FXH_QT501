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
from Ui_qt_003 import Ui_qt003

import wordcloud   #pip install wordcloud
import jieba     #pip install jieba
import imageio    #pip install imageio

#调用 QT 设计的界面对应的类
class W003(QDialog):
    def __init__(self, parent=None):        
        super(W003, self).__init__(parent)
        self.child = Ui_qt003()
        self.child.setupUi(self)
        self.child.btn_select_file.clicked.connect(self.select_file)
        self.child.btn_select_file_probit.clicked.connect(self.select_file_probit)
        self.child.btn_cloud.clicked.connect(self.gen_word_cloud)
        self.child.btn_select_file_2.clicked.connect(self.select_file2)
        self.child.btn_show_pic.clicked.connect(self.show_pic_orig)

    # 设立函数，来取得当前时间
    def get_sysdate(self):
        now = time.strftime("%Y%m%d %H%M%S", time.localtime(time.time()))
        # print(now)
        return now

    def select_file(self):
        fileName, filetype = QFileDialog.getOpenFileName(self, "选择文件", "/", "All Files (*);;TXT Files (*.txt)") # User 选择路径来找到文本文件
        # print(fileName, filetype)  # 打印文件全部路径（包括文件名和后缀名）和文件类型
        self.child.t_file.setText(fileName)    #把文件的路径写在 Text 上

    def select_file_probit(self):
        fileName, filetype = QFileDialog.getOpenFileName(self, "选择文件", "/", "All Files (*);;TXT Files (*.txt)") # User 选择路径来找到文本文件
        # print(fileName, filetype)  # 打印文件全部路径（包括文件名和后缀名）和文件类型
        self.child.t_file_probit.setText(fileName)    #把文件的路径写在 Text 上
    
    def select_file2(self):
        fileName, filetype = QFileDialog.getOpenFileName(self, "选择文件", "/", "All Files (*);;PNG Files (*.png)") # User 选择路径来找到图片
        # print(fileName, filetype)  # 打印文件全部路径（包括文件名和后缀名）和文件类型
        self.child.t_file_2.setText(fileName)    #把文件的路径写在 Text 上

    def show_pic_orig(self):
        filename2=self.child.t_file_2.text()
        if filename2=='':
            pass
        else:
            self.child.lbl_pic_orig.setPixmap(QPixmap(filename2))  # 在label上显示图片
            self.child.lbl_pic_orig.setScaledContents (True) # 让图片自适应label大小

    def gen_word_cloud(self):
        #取得文件名
        filename=self.child.t_file.text()
        #背景图的文件名
        pic_filename=self.child.t_file_2.text()

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

        #再 取得 禁用 内容
        #取得文件名        
        filename_probit=self.child.t_file_probit.text()
        new_stop_word_list = []
        if filename_probit=='':
            pass
        else:
            fr = open(filename_probit, 'r',encoding='GB18030', errors='ignore')
            stop_word_list = fr.readlines()        
            for stop_word in stop_word_list:
                stop_word = stop_word.replace('\ufeef', '').strip()
                new_stop_word_list.append(stop_word)
        print(new_stop_word_list)  #输出停用词

        #取得正文
        filename=self.child.t_file.text()
        fr_init=open(filename,'r',encoding='GB18030', errors='ignore')    
        s=fr_init.read()
        words=jieba.cut(s,cut_all=False)
        word_dict={}
        word_list=''
        for word in words:
            if (len(word) > 1 and not word in new_stop_word_list):
                word_list = word_list + ' ' + word
                if (word_dict.get(word)):
                    word_dict[word] = word_dict[word] + 1
                else:
                    word_dict[word] = 1
        fr.close()

         #按次数进行排序
        sort_words=sorted(word_dict.items(),key=lambda x:x[1],reverse=True)
        # print(sort_words[0:101])#输出前0-100的词
        new_word=''
        for x in sort_words[0:100]:       
            new_word=new_word+' '+ x[0]
        print(new_word)

        # 词云都是词语 显示      
        if pic_filename=='':
            w = wordcloud.WordCloud(width=1000,height=700,background_color='white',contour_width=1,font_path="C:/Windows/Fonts/STFANGSO.TTF")
            print('no pic')
        else:
            mk = imageio.imread(pic_filename)
            w = wordcloud.WordCloud(width=1000,height=700,background_color='white',mask=mk,contour_width=1,font_path="C:/Windows/Fonts/STFANGSO.TTF")
            print('pic')
 
        # w.generate(word_list)
        w.generate(new_word)
        w.to_file(file)

        #把file显示出来
        #显示图片
        self.child.lbl_pic.setPixmap(QPixmap(file))  # 在label上显示图片
        self.child.lbl_pic.setScaledContents (True) # 让图片自适应label大小

if __name__ == "__main__":    
    app = QApplication(sys.argv)
    my003 = W003()    
    my003.show()
    sys.exit(app.exec_())        