# 스레드사용 커스텀시그널 동작
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import * 

class Worker(QThread): 
    valChangeSignal = pyqtSignal(int)
    logChangeSignal = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.working = True

    def run(self):
        # 스레드로 동작할 내용
        # self.parent.pgbTask.setRange(0,99)
        while self.working:
            for i in range(0, 100):
                print(f'출력 > {i}')
                self.valChangeSignal.emit(i)
                time.sleep(0.0001)
                # self.parent.pgbTask.setValue(i) 
                # self.parent.txbLog.append(f'출력 > {i}')

class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('./windows/ui/threadtask.ui', self)
        self.btnStart.clicked.connect(self.btnStartClicked)
        # Worker 클래스가 가지고 있는 valChangeSignal 설정
        self.th = Worker(self)
        self.th.valChangeSignal.connect(self.updateProgress) # 슬롯정의
        self.th.logChangeSignal.connect(self.updateLog)
        self.show()
    
    @pyqtSlot(int) # decorator
    def updateProgress(self, val):
        self.pgbtasksetValue(self, val)
        self.txbLogappend(f'출력 > {val}')
        if val == 99:
            self.th.working.working = False

    @pyqtSlot(int)    
    def btnStartClicked(self):
        self.pgbTask.setRange(0,9999)
        # th = Worker(self)
        self.th.start()
        self.th.working = True

if __name__=='__main__':
    app = QApplication(sys.argv)
    win = MyApp()
    app.exec()