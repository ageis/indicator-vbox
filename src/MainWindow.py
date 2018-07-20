#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/20/18 10:56 AM
# @Author  : septemberhx
# @Site    : 
# @File    : MainWindow.py
# @Description:

from typing import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from VBox import VBox


class MainWindow(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.trayIcon = QSystemTrayIcon(QIcon.fromTheme("virtualbox"))
        self.menu = QMenu()
        self.actionDict = {}  # type: Dict[str, QAction]
        self.vm_state = {}  # type: Dict[str, bool]
        self.trayIcon.setContextMenu(self.menu)
        self.vboxTool = VBox()
        self.trayIcon.activated.connect(self.update_menu)
        self.create_menu()

    def create_menu(self):
        # self.exit_action = QAction('quit', self)
        # self.menu.addSeparator()
        # self.menu.addAction(self.exit_action)

        # Get the list of VM's
        vm_list = self.vboxTool.get_vm_list()
        for vm_name in vm_list:
            if len(vm_name) == 0:
                continue
            self.add_vm_to_tray(vm_name)
        self.update_menu()

    def update_menu(self):
        print('update menu...')
        self.vboxTool.update()
        for vm_name in self.actionDict.keys():
            is_running = self.vboxTool.is_vm_running(vm_name)
            print(vm_name, is_running)
            if is_running != self.vm_state[vm_name]:
                self.set_action_icon(is_running, self.actionDict[vm_name])
                self.vm_state[vm_name] = is_running

    def show(self):
        self.trayIcon.show()

    def hide(self):
        self.trayIcon.hide()

    def add_vm_to_tray(self, name):
        action = QAction(name, self)
        action.triggered.connect(self.action_triggerd)
        self.actionDict[name] = action
        self.menu.addAction(action)
        self.vm_state[name] = self.vboxTool.is_vm_running(name)
        self.set_action_icon(self.vm_state[name], self.actionDict[name])

    def remove_vm_from_tray(self, name):
        if name in self.actionDict:
            self.menu.removeAction(self.actionDict[name])
            self.actionDict.pop(name)

    def set_action_icon(self, is_running, action):
        if is_running:
            action.setIcon(QIcon.fromTheme("system-run"))
        else:
            action.setIcon(QIcon.fromTheme("system-suspend"))

    def action_triggerd(self):
        vm_name = self.sender().text()
        if self.vm_state[vm_name]:
            try:
                self.vboxTool.suspend_VM(vm_name)
            except Exception as e:
                self.trayIcon.showMessage('Failed', 'Failed to suspend VM {0}. {1}'.format(vm_name, e))
            else:
                self.trayIcon.showMessage('Succeed', 'Succeed to suspend VM {0}'.format(vm_name))
        else:
            try:
                self.vboxTool.launch_VM(vm_name)
            except Exception as e:
                self.trayIcon.showMessage('Failed', 'Failed to start VM {0}. {1}'.format(vm_name, e))
            else:
                self.trayIcon.showMessage('Succeed', 'Succeed to start VM {0}'.format(vm_name))
        self.update_menu()