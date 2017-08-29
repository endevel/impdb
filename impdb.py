#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QWidget

from gui.mainform import MainForm

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mf = MainForm()
    mf.show()
    sys.exit(app.exec_())

