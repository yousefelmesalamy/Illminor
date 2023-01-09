from views import heart_model
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *


class Heart_MANGER(QtWidgets.QWidget, heart_model.Ui_Form):
    acceptedSignal = pyqtSignal()
    def __init__(self):
        super(Heart_MANGER, self).__init__()
        self.setupUi(self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = Heart_MANGER()
    window.show()
    app.exec_()
