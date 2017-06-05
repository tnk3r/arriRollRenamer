#!/usr/bin/python

from PyQt4.QtGui import QMainWindow, QApplication, QFileDialog, QDialog, QPushButton, QLabel, QLineEdit
from PyQt4.QtCore import QString
import os, sys
controller = QApplication(sys.argv)

class window(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=None)
        self.files = str(QFileDialog.getExistingDirectory(self, "Select Directory containing Resolve DPX stills"))
        self.Error = QString("")
        self.showdialog("Set New Roll Number")
        #self.process_frames()
        sys.exit(0)

    def showdialog(self, title):
        d = QDialog(self)
        d.setFixedSize(300, 100)
        label = QLabel(self.Error, d)
        label.move(20, 20)
        self.current = os.listdir(self.files)[0][0:4]
        self.roll = QLineEdit(str(self.current), d)

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
            with open(str(file), "r+b") as f:
                if str(f.read(4)) == "ARRI":
                    f.seek(1272)
                    f.write(self.newRoll)
                    f.seek(1688)
                    f.write(self.newRoll)
                    f.close
            os.system("mv "+str(file)+" "+str(self.newRoll)+str(file)[4:])
        os.system("mv "+str(self.files)+" "+str(os.path.dirname(self.files))+"/"+str(self.newRoll)+str(self.files.split("/")[-1])[4:])
        controller.quit()


main = window()
main.show()
main.raise_()
sys.exit(controller.exec_())
