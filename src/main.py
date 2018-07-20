#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/20/18 10:39 AM
# @Author  : septemberhx
# @Site    : 
# @File    : main.py.py
# @Description: main function

import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Virtualbox Indicator")
    mainWindow = MainWindow()
    mainWindow.show()

    mainWindow.add_vm_to_tray("Win10")
    mainWindow.remove_vm_from_tray("Win10")
    exit(app.exec())