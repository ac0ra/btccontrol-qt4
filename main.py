#!/usr/bin/python


__author__ = 'adam'
version = "0.0.1"
title = 'BTC Control v'+version
import sys
from PyQt4 import QtGui



class MainWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.setGeometry(0,0, 800,600)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.resize(800,600)
        self.setMinimumSize(800,600)
        self.center()

        #-- menu --#
        open = QtGui.QAction("Exit", self)
        save = QtGui.QAction("Save", self)
        build = QtGui.QAction("Build", self)
        exit = QtGui.QAction("Quit", self)
        about = QtGui.QAction("About", self)
        donate = QtGui.QAction("Donate", self)
        actualhelp = QtGui.QAction("Actual Help", self)

        menu_bar = QtGui.QMenuBar()
        file = menu_bar.addMenu("&File")
        help = menu_bar.addMenu("&Help")

        file.addAction(open)
        file.addAction(save)
        file.addAction(build)
        file.addAction(exit)

        help.addAction(about)
        help.addAction(donate)
        help.addAction(actualhelp)

        tab_widget = QtGui.QTabWidget()
        tab1 = QtGui.QWidget()
        tab2 = QtGui.QWidget()
        tab3 = QtGui.QWidget()
        tab4 = QtGui.QWidget()

        p1_vertical = QtGui.QVBoxLayout(tab1)
        p2_vertical = QtGui.QVBoxLayout(tab2)
        p3_vertical = QtGui.QVBoxLayout(tab3)
        p4_vertical = QtGui.QVBoxLayout(tab4)

        tab_widget.addTab(tab1, "Summary")
        tab_widget.addTab(tab2, "Trading")
        tab_widget.addTab(tab3, "Mining")
        tab_widget.addTab(tab4, "Settings")

        button1 = QtGui.QPushButton("update")
        p1_vertical.addWidget(button1)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(menu_bar)
        vbox.addWidget(tab_widget)

        self.setLayout(vbox)

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)




app = QtGui.QApplication(sys.argv)
frame = MainWindow()
frame.show()
sys.exit(app.exec_())