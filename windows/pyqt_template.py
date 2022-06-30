# PyQt 템플릿 소스
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import * 

class MyApp(QMainWindow): # QMainWindow 변경요
    def __init__(self):
        super(MyApp, self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('./windows/ui/threadtask.ui', self) # UI파일 변경요
        # TODO 로직은 여기에 작성
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    win = MyApp()
    app.exec()