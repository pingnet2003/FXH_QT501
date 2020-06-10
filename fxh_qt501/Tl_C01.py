import sys
import time
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets
# from PyQt5.QtWidgets import QTableWidget, QProgressBar, QLineEdit, QComboBox, QFrame, QTableWidgetItem
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# 这个test_pyqt是ui文件对应的py文件的文件名
from Ui_qt_C01 import Ui_qtC01

from PIL import Image, ImageDraw, ImageFont   #pip3 install pillow

# 调用 QT 设计的界面对应的类

# 指定要使用的字体和大小
font = ImageFont.truetype("C:/Windows/Fonts/STFANGSO.TTF", 24)

class WC01(QDialog):
    def __init__(self, parent=None):
        super(WC01, self).__init__(parent)
        self.child = Ui_qtC01()
        self.child.setupUi(self)
        self.child.btn_select_file.clicked.connect(self.select_file)
        # self.child.btn_show_pic.clicked.connect(self.show_pic_orig)
        self.child.btn_Watermark.clicked.connect(self.add_watermark)

    # 设立函数，来取得当前时间

    def get_sysdate(self):
        now = time.strftime("%Y%m%d %H%M%S", time.localtime(time.time()))
        # print(now)
        return now

    def select_file(self):
        fileName, filetype = QFileDialog.getOpenFileName(
            self, "选择文件", "/", "All Files (*);;jpg Files (*.jpg)")  # User 选择路径来找到图片文件
        # print(fileName, filetype)  # 打印文件全部路径（包括文件名和后缀名）和文件类型
        self.child.t_file.setText(fileName)  # 把文件的路径写在 Text 上
        self.show_pic_orig()

    def show_pic_orig(self):
        filename2 = self.child.t_file.text()
        if filename2 == '':
            pass
        else:
            self.child.lbl_pic_orig.setPixmap(
                QPixmap(filename2))  # 在label上显示图片
            self.child.lbl_pic_orig.setScaledContents(True)  # 让图片自适应label大小
    
    # image: 图片  text：要添加的文本 font：字体
    def add_text_to_image(self,image, text, font=font):
        #图像类型转换
        rgba_image = image.convert('RGBA')        
        #创建新图片 Image.new(mode,size,color)   #查看图像信息 im.size        
        text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))  
        #创建一个可以在给定图像上绘图的对象
        image_draw = ImageDraw.Draw(text_overlay)
        #返回给定字符串的大小，以像素为单位。 draw.textsize(string,options)⇒ (width, height)
        #变量option的font用于指定所用字体。它应该是类ImangFont的一个实例，使用ImageFont模块的load()方法从文件中加载的
        text_size_x, text_size_y = image_draw.textsize(text, font=font)        
        # print(rgba_image)
        # 开始判断水印位置
        if self.child.rb_1.isChecked()==True:
            text_xy= (3,3)   # 左上角
        if self.child.rb_2.isChecked()==True:
            text_xy= (rgba_image.size[0] - text_size_x,3)  # 右上角  
        if self.child.rb_3.isChecked()==True:
            text_xy= (3,rgba_image.size[1] - text_size_y)  # 左下角
        if self.child.rb_4.isChecked()==True:
            text_xy = (rgba_image.size[0] - text_size_x,  # 右下角  
                   rgba_image.size[1] - text_size_y)   
        # 在给定的位置绘制一个字符创。draw.text(position,string, options)
        # 变量position给出了文本的左上角的位置。
        # 变量option的font用于指定所用字体
        # 变量options的fill给定文本的颜色。
        image_draw.text(text_xy, text, font=font, fill=(76, 234, 124, 180))
        # Image.alpha_composite(im1,im2) 将im2复合到im1上，返回一个Image对象
        # im1和im2的size要相同。且im1和im2的mode都必须是RGBA
        image_with_text = Image.alpha_composite(rgba_image, text_overlay)

        return image_with_text

    def add_watermark(self):
        pic_file = self.child.t_file.text()
        pic_text = self.child.t_text.text()
        if pic_file == '' or pic_text =='':
            reply = QMessageBox.information(
                self, '提醒', '图片 或 水印文字 为空,请检查并补录完整', QMessageBox.Yes, QMessageBox.Yes)
        else:
             #分离出文件路径及文件名
            if pic_file=='':
                filepath='e://'
                tempfilename=self.get_sysdate()+'.png'
            else:
                (filepath,tempfilename)=os.path.split(pic_file)
                (tempfilename,extension)=os.path.splitext(tempfilename)
                tempfilename=tempfilename+self.get_sysdate()+'.png'
                file=os.path.join(filepath,tempfilename)
                self.child.t_aim_file.setText(file)

            im_before = Image.open(pic_file)   #读取一张图片
            # im_before.show()    # 显示一张图片              
            im_after = self.add_text_to_image(im_before, pic_text)            
            im_after.save(file)    #保存图片                   
            #显示图片
            self.child.lbl_pic.setPixmap(QPixmap(file))  # 在label上显示图片
            self.child.lbl_pic.setScaledContents (True) # 让图片自适应label大小

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myc01 = WC01()
    myc01.show()
    sys.exit(app.exec_())
