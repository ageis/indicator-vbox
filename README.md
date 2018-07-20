## VirtualBox Indicator Applet

Rewrite with PyQt5 and Python3

Launch/suspend your virtual machine created by virtualbox through tray icon.

gtk version:  [click here](https://github.com/yurigorokhov/indicator-vbox)

### python module needed:

* pyqt5
* typing

### install & run

```shell
git clone https://github.com/SeptemberHX/indicator-vbox.git
cd indicator-vbox
sudo make install
/opt/indicator-vbox/indicator-vbox
```

### uninstall

```shell
cd indicator-vbox
sudo make uninstall
```

### usage

left/middle click to refresh the machine list in the menu

Launch/suspend machine by clicking target machine's name

### screenshot

![screenshot](https://github.com/SeptemberHX/indicator-vbox/blob/master/screenshot_new.png)

--------------------------------------------

VirtualBox Indicator Applet

INSTALL
--------------------------------------------

To install simply run this command
> sudo make install

This will install the executable indicator-vbox into /usr/local/bin by default.
Edit the install.sh file if you want a different location.

UNINSTALL
--------------------------------------------

To uninstall simply type:
> sudo make uninstall

CONTACT
--------------------------------------------

Yuri Gorokhov
yurigorokhov@gmail.com

