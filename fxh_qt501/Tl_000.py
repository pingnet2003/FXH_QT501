import sys
from Ui_qt_000  import Ui_MainWindow
import Tl_001,Tl_002,Tl_003
import Tl_A01,Tl_A02
import Tl_D01
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets

class w000(QMainWindow):
    def __init__(self,parent=None):
        super(w000,self).__init__(parent)
        self.child = Ui_MainWindow()
        self.child.setupUi(self)
        self.child.btn_001.clicked.connect(self.call_001)
        self.child.btn_002.clicked.connect(self.call_002)
        self.child.btn_003.clicked.connect(self.call_003)

        self.child.btn_A01.clicked.connect(self.call_A01)
        self.child.btn_A02.clicked.connect(self.call_A02)

        self.child.btn_D01.clicked.connect(self.call_D01)
        
    
    #调出词云所在的 PY
    def call_001(self):
        pass
        self.cw001 = Tl_001.W001()
        self.cw001.exec()  

    #调出 九宫格 所在的 PY
    def call_002(self):
        pass
        self.cw002 = Tl_002.MyWindow()
        self.cw002.show()  

    #调出词云  所在的 PY
    def call_003(self):
        pass
        self.cw003 = Tl_003.W003()
        self.cw003.show()          

    #调出Baidu 图片下载所在的 PY
    def call_A01(self):
        pass
        self.cwA01 = Tl_A01.c_tl_a01()
        self.cwA01.show()        
 
    #调出 you-get 下载视频 所在的 PY
    def call_A02(self):
        pass
        self.cwA02 = Tl_A02.c_tl_a02()
        self.cwA02.show()   

    #调出数据库 TableGrid 的 PY
    def call_D01(self):
        pass
        self.cwD01 = Tl_D01.MyWindow()
        self.cwD01.show()        


if __name__ == "__main__":    
    app = QApplication(sys.argv)
    my000 = w000()    
    my000.show()
    sys.exit(app.exec_())   