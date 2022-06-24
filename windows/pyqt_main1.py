## PYQT 학습
from PyQt5.QtWidgets import *
import sys

def run():
   app = QApplication(sys.argv) # app 객체 생성

   label = QLabel('\tHello .Qt5!!') # 라벨위젯 생성
   wnd = QMainWindow() # window 객체생성 QWidget, QDialog
   wnd.setWindowTitle('First PyQt') # 
   wnd.setCentralWidget(label) # 윈도우 정중앙 위치
   wnd.show() # 3
   app.exec_() # 4


if __name__ == '__main__':
   run()