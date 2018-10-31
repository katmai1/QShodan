#!/usr/bin/python3

from PyQt5 import QtWidgets
from ui.mainwin import MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
