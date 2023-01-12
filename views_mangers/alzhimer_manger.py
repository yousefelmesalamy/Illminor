from views import alzhimer_model
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
import requests

# response = requests.get(http://illacc.pythonanywhere.com/alzheimer")
class Alzahimer_MANGER(QtWidgets.QWidget, alzhimer_model.Ui_Form):
    acceptedSignal = pyqtSignal()
    def __init__(self):

        super(Alzahimer_MANGER, self).__init__()
        self.setupUi(self)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = Alzahimer_MANGER()
    window.show()
    app.exec_()
