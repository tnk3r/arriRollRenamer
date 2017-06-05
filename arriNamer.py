#!/usr/bin/python

from PyQt4.QtGui import QMainWindow, QApplication, QFileDialog, QDialog, QPushButton, QLabel, QLineEdit
from PyQt4.QtCore import QString
import os, sys

controller = QApplication(sys.argv)

class window(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=None)
        self.files = str(QFileDialog.getExistingDirectory(self, "Select ARRIRAW Clip Directory"))
        self.Error = QString("")
        if self.files != "":
            self.showdialog("Set New Roll Number")
        sys.exit(0)

    def showdialog(self, title):
        d = QDialog(self)
        d.setFixedSize(300, 100)
        label = QLabel(self.Error, d)
        label.move(20, 20)
        self.current = os.listdir(self.files)[0][0:4]
        self.roll = QLineEdit(str(self.current), d)
        self.roll.move(50, 20)

        b1 = QPushButton("Ok",d)
        b1.move(125,50)
        d.setWindowTitle(str(title))

        b1.clicked.connect(self.process_frames)
        d.exec_()

    def process_frames(self):
        self.newRoll = str(self.roll.text()).strip()
        print self.newRoll
        os.chdir(self.files)
        for file in os.listdir(self.files):
            ari = 0
            with open(str(file), "r+b") as f:
                if str(f.read(4)) == "ARRI":
                    f.seek(1272)
                    if os.path.basename(file)[0:4] == f.read(4):
                        f.write(self.newRoll)
                        f.seek(1688)
                        f.write(self.newRoll)
                    f.close
                    ari = 1
            if ari == 1:
                os.system("mv "+str(file)+" "+str(self.newRoll)+str(file)[4:])
        controller.quit()


main = window()
main.show()
main.raise_()
sys.exit(controller.exec_())
