from views import diabetes_model
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *


class Diabetes_MANGER(QtWidgets.QWidget, diabetes_model.Ui_Form):
    acceptedSignal = pyqtSignal()
    def __init__(self):
        super(Diabetes_MANGER, self).__init__()
        self.setupUi(self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = Diabetes_MANGER()
    window.show()
    app.exec_()
