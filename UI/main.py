import sys
import iconify as ico
from iconify.qt import QtGui

# from PyQt5.uic import loadUi
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication

from loader import *

from PySide2.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        loadUi("UI\interface.ui", self)
        
        icon = ico.Icon('material-design:arrow-expand-right', color=QtGui.QColor('white'))
        self.menuBtn.setIcon(icon)
        icon = ico.Icon('material-design:home', color=QtGui.QColor('white'))
        self.homeBtn.setIcon(icon)
        icon = ico.Icon('material-design:file-document-box-multiple-outline', color=QtGui.QColor('white'))
        self.reportBtn.setIcon(icon)
        icon = ico.Icon('material-design:settings', color=QtGui.QColor('white'))
        self.settingsBtn.setIcon(icon)
        icon = ico.Icon('material-design:information', color=QtGui.QColor('white'))
        self.infoBtn.setIcon(icon)
        icon = ico.Icon('material-design:help-circle', color=QtGui.QColor('white'))
        self.helpBtn.setIcon(icon)
        icon = ico.Icon('feather:x', color=QtGui.QColor('white'))
        self.xcloseBtn.setIcon(icon)
        icon = ico.Icon('feather:square', color=QtGui.QColor('white'))
        self.squareBtn.setIcon(icon)
        icon = ico.Icon('feather:minus', color=QtGui.QColor('white'))
        self.minusBtn.setIcon(icon)
        icon = ico.Icon('material-design:reload', color=QtGui.QColor('white'))
        self.reloadBtn.setIcon(icon)
        icon = ico.Icon('feather:chevron-left', color=QtGui.QColor('white'))
        self.backBtn.setIcon(icon)
        icon = ico.Icon('feather:chevron-right', color=QtGui.QColor('white'))
        self.nextBtn.setIcon(icon)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

if __name__ == "__main__":
    # app = QApplication(sys.argv)
    
    # mainwindow = MainWindow()
    # widget = QtWidgets.QStackedWidget()
    # widget.addWidget(mainwindow)
    # widget.setFixedHeight(850)
    # widget.setFixedWidth(1120)
    # widget.show()
    # try:
    #     sys.exit(app.exec_())
    # except:
    #     print("Exiting")
    
    main()