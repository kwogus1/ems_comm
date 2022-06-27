## LED Control UI
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import RPi.GPIO as GPIO
import time

SERVO = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO, GPIO.OUT)

pwm = GPIO.PWM(SERVO, 50)
pwm.start(3.0)

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('RPi Motol Control')
        # 윈도우 기본설정
        self.setGeometry(100, 100, 300, 350)

        self.dial = QDial(self)
        self.dial.setRange(0, 13)

        self.label = QLabel(self)
        self.label.setFont(QFont('Arial', 15))
        self.label.setText('LED Control')
        self.label.setAlignment(Qt.AlignCenter) #  LED Control 정중앙 위치

        # 시그널
        self.dial.valueChanged.connect(self.Dial_Changed)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.dial)
        self.vbox.addWidget(self.label)

        self.show()

    def Dial_Changed(self):
        self.label.setText(str(self.dial.value()))
        pwm.ChangeDutyCycle(float(self.dial.value()))

if __name__ =='__main__':
    app = QApplication(sys.argv)
    wnd = MyApp()
    app.exec_()