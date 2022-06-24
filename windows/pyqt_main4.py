# QLabel
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

class MyApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI() # 내가 만들 UI 초기화 함수

    def initUI(self):
        self.setWindowTitle('PyQt Widget2')
        self.setGeometry(490, 250, 300, 300)
        self.setWindowIcon(QIcon('lion.png')) 
        
        # Label작업시작
        label1, label2 = QLabel('LABEL1'), QLabel('라벨2')
        label1.setAlignment(Qt.AlignBottom)
        label1.setStyleSheet(
            ('border-width: 2px;'
             'border-style: solid;'
             'border-color: blue;'
             'image: url(./windows/images/image1.png)')
        )

        label2.setAlignment(Qt.AlignBottom)
        label2.setStyleSheet(
             ('border-width: 3px;'
             'border-style: dot-dot-dash;'
             'border-color: red;'
             'image: url(./windows/images/image2.png)')
        )


        hbox = QHBoxLayout(self)
        hbox.addWidget(label1)
        hbox.addWidget(label2)

        self.setLayout(hbox)        
        self.setGeometry(300, 200, 320, 230)
        self.setWindowTitle('QLabel!!')
        self.show()

        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    wnd = MyApp()

    app.exec_()