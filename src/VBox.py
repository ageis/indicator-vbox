#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
from typing import *

# Class for menu items
class VBoxImageMenuItem:
    is_vm = False
    state = 0 # 0 > suspended 1 > running
    
    def __init__(self, title, is_vm):
        self.is_vm = is_vm
        self.state = 0
    
    def set_state(self, state):
        self.state = state
        
    def get_state(self):
        return self.state
    
    def get_name(self):
        return "VBoxImageMenuItem"


# VirtualBox Class to interface with the program
class VBox:
    def __init__(self):
        # list of running vm's
        self.running_vms = []
        # existing VM's
        self.existing_vms = []  # type: List[str]
        self.update()
    
    # does vm exist?
    def exists(self, vm):
        return (self.existing_vms.count(vm) > 0)
    
    # Populate existing vms
    def populate_existing_vms(self):
        self.existing_vms.clear()
        for vm_name in subprocess.check_output("VBoxManage list vms | sed -e 's/^.*\\\"\(.*\)\\\".*$/\\1/'", shell=True).decode('utf-8').split('\n'):
            if len(vm_name) != 0:
                self.existing_vms.append(vm_name)
    
    # Retrieve the names of installed VM's
    def get_vm_list(self):
        return self.existing_vms
    
    # populate list of running vms
    def populate_running_vms(self):
        del self.running_vms[:]
        for vm in self.get_vm_list():
            if(self.__vm_running(vm) == 1):
                self.running_vms.append(vm)
    
    # Check if a vm is running by querying running_vms[]
    def is_vm_running(self, vm):
        return (self.running_vms.count(vm) > 0)
    
    # Check if a vm is running
    def __vm_running(self, vmname):
        output = subprocess.check_output("VBoxManage showvminfo \"" + vmname + "\" | grep State", shell=True).decode('utf-8')
        if(output.count("running") > 0):
            return 1
        else:
            return 0  
    
    # Suspend all running vms
    def suspend_all_running(self):
        self.populate_running_vms()
        ret_code = 0
        for vm in self.running_vms:
            ret_code = self.suspend_VM(vm)
        return ret_code
    
    def launch_VBox(self):
        return subprocess.call(["VirtualBox"])
    
    # Suspend VM by name
    def suspend_VM(self, vmname):
        return subprocess.call(["VBoxManage", "controlvm", vmname,"savestate"])
        
    # Launch a VM by name
    def launch_VM(self, vmname):
        return subprocess.call(["VBoxManage", "startvm", vmname])
    
    # Update lists
    def update(self):
        self.populate_running_vms()
        self.populate_existing_vms()
        