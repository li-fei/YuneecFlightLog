# -*- coding: utf-8 -*-

"""
PyQt5 tutorial

In this example, we determine the event sender
object.

author: py40.com
last edited: 2017年3月
"""
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QPushButton,
                             QAction, QFileDialog, QApplication, QLineEdit)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.btn = QPushButton('open', self)
        self.btn.move(40, 40)
        self.btn.clicked.connect(self.openFile)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(40,200)

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(40, 80, 200, 100))

        # self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 100, 500, 500)
        self.setWindowTitle('File dialog')
        self.show()


    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

    def openFile(self):
        print("openFile ...")
        self.showDialog()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())