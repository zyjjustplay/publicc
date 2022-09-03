import os
import sys,pyperclip,time
import threading
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from ui_copy import Ui_maincopy
from PySide6.QtGui import *

path = os.path.realpath(os.curdir)#获取当前目录的绝对路径
class my_thread(QThread):
    signal=Signal()
    def __init__(self):
        super(my_thread,self).__init__()
        self.is_quit=0
    def run(self):
        while self.is_quit==0:
            self.signal.emit()
            QThread.sleep(1)
        self.quit()
class Word(QMainWindow, Ui_maincopy):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.copyn.clicked.connect(self.copys)
        self.showtimea.clicked.connect(self.stime)
        self.pastelabel.setWordWrap(True)
        self.pastelabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.getcopy.setLineWrapMode(QPlainTextEdit.NoWrap)
        sb=QMessageBox.question(self,"hi","看不看粘贴板?",QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        self.show()
        if(sb==QMessageBox.Yes):
            self.thread2=my_thread()
            self.thread2.signal.connect(self.paste1)
            self.thread2.start()
        else:
            self.pastelabel.setText("你不想显示我就不显示")
    def closeEvent(self,event):
        os._exit(0)
    def copys(self):
        if(self.getcopy.toPlainText()!=""):
            ans=self.getcopy.toPlainText()
            pyperclip.copy(ans)
            QMessageBox.information(self,"hei","拷贝成功")
            self.getcopy.clear()
    def paste1(self):
        self.pastelabel.setText(pyperclip.paste())
    def paste2(self):
        while True:
            self.pastelabel.setText(pyperclip.paste())
            QThread.sleep(1)
    def cana(self):
        t=threading.Thread(target=self.paste2)
        t.setDaemon(True)
        t.start()
    def stime(self):
        os.popen("E:/ForWindowsC/word/dist/time/time.exe")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Word()
    sys.exit(app.exec())
