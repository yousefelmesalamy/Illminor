from views import blood_model
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *


class Blood_MANGER(QtWidgets.QWidget, blood_model.Ui_Form):
    acceptedSignal = pyqtSignal()
    def __init__(self):
        super(Blood_MANGER, self).__init__()
        self.setupUi(self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = Blood_MANGER()
    window.show()
    app.exec_()
