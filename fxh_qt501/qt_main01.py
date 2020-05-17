import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets
# from PyQt5.QtWidgets import QTableWidget, QProgressBar, QLineEdit, QComboBox, QFrame, QTableWidgetItem
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# 这个test_pyqt是ui文件对应的py文件的文件名
from Ui_test02 import Ui_test_form1

# 我的Form是用的QWidget作为基类

# 全局字体 
light_10_font = QtGui.QFont()
light_10_font.setFamily("微软雅黑 Light")
light_10_font.setPointSize(10)
light_10_font.setBold(False)
light_10_font.setWeight(50)

light_12_font = QtGui.QFont()
light_12_font.setFamily("微软雅黑 Light")
light_12_font.setPointSize(12)
light_12_font.setBold(False)
light_12_font.setWeight(50)

class MyWindow(QWidget, Ui_test_form1):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.SetDailyTableColumns()
        self.btn_read.clicked.connect(self.p_readData)   #按钮对应的 函数

    def SetDailyTableColumns(self):
        rtn_desc, rtn_prop = self.select_prop()  # 取得数据
        col_len = len(rtn_prop[0])  # 取得返回结果的 列数
        #TW_01 是 Qtable Widget 对象
        self.TW_01.setColumnCount(col_len)  # 设置列数
        self.TW_01.setRowCount(len(rtn_prop))  # 设置共有几行
        self.TW_01.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置 表格内容 不允许更改

        for i in range(len(rtn_desc)):  # 设置标题
            item_header= QtWidgets.QTableWidgetItem(rtn_desc[i][0])
            item_header.setFont(light_12_font)    #设置标题的 字体
            item_header.setTextAlignment(QtCore.Qt.AlignCenter)  #设置中间对齐
            self.TW_01.setHorizontalHeaderItem(i, item_header)

         # 设置 内容
        for row in range(len(rtn_prop)):    # 设置行
            for col in range(len(rtn_prop[row])):   # 设置列                
                Item_value = QtWidgets.QTableWidgetItem(
                    str(rtn_prop[row][col]))  # 格式化值
                Item_value.setFont(light_10_font)    #设置内容的 字体
                Item_value.setTextAlignment(QtCore.Qt.AlignLeft)   #设置左对齐
                self.TW_01.setItem(row, col, Item_value)  # 设置值

        # self.TW_01.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)   #本意是设置按内容自适应宽度，待验证

        # 设置 标题 的样式
        self.TW_01.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:lightblue;color: black;padding-left: 4px;border: 1px solid#6c6c6c;}")  
        self.TW_01.verticalHeader().setHidden(False)  # 显示行号

        # Item_2 = QtWidgets.QTableWidgetItem('Row2')  # 格式化值
        # self.TW_01.verticalHeader().setVerticalHeaderItem(2, item)  #本意是设置 行头的 标题，待验证

        # 以下可用,但本案例没有使用到
        # self.TW_01.verticalHeader().setHidden(True)    #隐藏行号方法
        # self.TW_01.horizontalHeader().hide()  #隐藏列头方法
        # self.TW_01.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents);     #设置第6列要根据内容使用宽度的列
        # self.TW_01.horizontalHeader().resizeSection(0, 200)  # 调整第一列的大小为100像素

    def p_readData(self):
        print('data')
        # self.TW_01.setCurrentCell(1, 1, QItemSelectionModel.Select)   #设置让 第二行，第二列 选中
        self.TW_01.setCurrentCell(1,0, QItemSelectionModel.Select)   #设置让 第二行 整行 选中
        

    def select_prop(self):
        # 连接Sqlite  数据库
        try:
            database=sqlite3.connect("rasppi01.db")
            cursor=database.cursor()
            sql="select pi_name,pi_ip,clam,bug_cnt,scan_date,main_date,daily_date,engine_ver,known_virus,pi_cpu_serial,sys_date from pi_prop order by pi_name"
            cursor.execute(sql)
            data_desc=cursor.description
            data_value=cursor.fetchall()
            print(data_value)
        except:
            import sys
            tuple=sys.exc_info()
            errmsg=' Failure querying pi_prop ,'+' Error:'+str(tuple[1])
            print(errmsg)
            # tkinter.messagebox.showerror(title='Failure ', message=errmsg)
        finally:
            database.close()
            # print(data_value)
            return data_desc, data_value


if __name__ == "__main__":
    app=QApplication(sys.argv)
    w=MyWindow()
    w.resize(900, 300)
    w.show()
    sys.exit(app.exec_())
