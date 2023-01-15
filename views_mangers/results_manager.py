from views import results_view
from PyQt5 import QtWidgets
import requests
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *


class RESULTS_MANAGER(QtWidgets.QWidget, results_view.Ui_Form):
    def __init__(self):
        super(RESULTS_MANAGER, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = RESULTS_MANAGER()
    window.show()
    app.exec_()
