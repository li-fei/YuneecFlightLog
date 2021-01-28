#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Py40 PyQt5 tutorial

In this example, we position two push
buttons in the bottom-right corner
of the window.

author: Jan Bodnar
website: py40.com
last edited: January 2015
"""

import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        noButton = QPushButton("NO")

        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        # hbox.addStretch(1)
        hbox.addWidget(okButton)
        # hbox.addWidget(noButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.setSpacing(100)
        # vbox.addStretch(0)
        vbox.addLayout(hbox)
        vbox.addWidget(noButton)
        vbox.setContentsMargins(10,0,0,0)
        # vbox.set

        self.setLayout(vbox)

        self.setGeometry(300, 300, 600, 350)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())