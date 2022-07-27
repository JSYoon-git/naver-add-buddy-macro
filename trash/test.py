#threading을 이용해 쓰레드 구현
from PyQt5.QtWidgets import QWidget
import threading
import time
import sys

a, b = 0, 0

#쓰레드 선언
class Thread1(QWidget.QThread):
    def __init__(self, num):
        super().__init__()
        global a, b
        self.a = a
        self.b = b
        self.num = num
    def run(self):
        
        for i in range(self.num):
            print("Thread :",i)
            self.a = self.a + 1
            self.b = self.b + 2
            time.sleep(1)


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        thread_start = QPushButton("시 작!")
        thread_start.clicked.connect(self.increaseNumber)

        vbox = QVBoxLayout()
        vbox.addWidget(thread_start)

        self.resize(200,200)
        self.setLayout(vbox)

    def increaseNumber(self):
        x = Thread1(10)
        print(x.b)
        x.setDaemon(True)
        x.start()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec_())