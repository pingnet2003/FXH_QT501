import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtGui, QtCore, QtWidgets
# from PyQt5.QtWidgets import QTableWidget, QProgressBar, QLineEdit, QComboBox, QFrame, QTableWidgetItem
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Ui_qt_E01 import Ui_Frm_Excel_Import
import os
import time

# 我的Form是用的QWidget作为基类


class MyWindow(QWidget, Ui_Frm_Excel_Import):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_select.clicked.connect(self.select_excel)
        self.btn_import.clicked.connect(self.excel_import)

    # 设立函数，来取得当前时间
    def get_sysdate(self):
        now = time.strftime("%Y%m%d %H%M%S", time.localtime(time.time()))
        # print(now)
        return now

    def select_excel(self):
        fileName, filetype = QFileDialog.getOpenFileName(
            self, "选择文件", "/", "All Files (*);;Excel 2003 Files (*.xls);;Excel 2007 Files (*.xlsx)")  # User 选择路径来找到图片
        print(fileName, filetype)  # 打印文件全部路径（包括文件名和后缀名）和文件类型
        self.t_directory.setText(fileName)  # 把图片的路径写在 Text 上

    def excel_import(self):
        db_name=self.t_db_name.text()
        if db_name=="" :
            reply = QMessageBox.warning(self,'警告','DB Name 栏位为空,请输入',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        
        excel_file=self.t_directory.text()
        if excel_file=="":
            reply = QMessageBox.warning(self,'警告','Excel File 栏位为空,请输入或选择一个文件',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)


        reply = QMessageBox.question(
            self, '确认', '是否要把Excel资料导入到'+db_name+'中?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.resize(900, 800)
    w.show()
    sys.exit(app.exec_())
