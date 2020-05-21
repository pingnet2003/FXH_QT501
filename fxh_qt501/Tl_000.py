import sys
from Ui_qt_000  import Ui_MainWindow
import Tl_001
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets

class w000(QMainWindow):
    def __init__(self,parent=None):
        super(w000,self).__init__(parent)
        self.child = Ui_MainWindow()
        self.child.setupUi(self)
        self.child.btn_001.clicked.connect(self.call_001)
    
    #调出词云所在的 PY
    def call_001(self):
        pass


if __name__ == "__main__":    
    app = QApplication(sys.argv)
    my000 = w000()    
    my000.show()
    sys.exit(app.exec_())   