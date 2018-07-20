INSTALL_DIR=/opt/indicator-vbox
VERSION=1.3

install:
	mkdir -p ${INSTALL_DIR}
	install -m 644 ./images/* /usr/share/pixmaps/
	install -m 644 ./src/main.py ${INSTALL_DIR}/indicator-vbox
	install -m 644 ./src/MainWindow.py ${INSTALL_DIR}/
	install -m 644 ./src/VBox.py ${INSTALL_DIR}/
	chmod +x ${INSTALL_DIR}/indicator-vbox

uninstall:
	rm -r -f /usr/share/pixmaps/VBox-gray.png
	rm -r -f ${INSTALL_DIR}

dist:
	mkdir indicator-vbox
	cp -r -f Makefile README.md src images screenshot.png screenshot_new.png indicator-vbox
	tar -c indicator-vbox > indicator-vbox-${VERSION}.tar
	gzip indicator-vbox-${VERSION}.tar
	rm -r -f indicator-vbox

clean:
	rm -r -f *.tar.gz